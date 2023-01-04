import sqlite3
import pandas as pd

def set_df(cnx):
	partida = pd.read_sql_query("SELECT * FROM Match", cnx)

	for i in range(1, 12):
		partida = partida.drop("home_player_X" + str(i), axis=1)
		partida = partida.drop("home_player_Y" + str(i), axis=1)
		partida = partida.drop("away_player_X" + str(i), axis=1)
		partida = partida.drop("away_player_Y" + str(i), axis=1)

	columns = ["goal", "shoton", "shotoff", "foulcommit", "card", "cross", "corner", "possession", "id", "B365H", "B365D", "B365A", "BWH", "BWD", "BWA", "IWH",
			"IWD", "IWA", "LBH", "LBD", "LBA", "PSH", "PSD", "PSA", "WHH", "WHD", "WHA", "SJH", "SJD", "SJA", "VCH", "VCD", "VCA", "GBH", "GBD", "GBA", "BSH", "BSD", "BSA"]

	columns += ["country_id", "league_id", "stage", "match_api_id", "home_team_goal", "away_team_goal"]

	for column in columns:
		partida = partida.drop(column, axis=1)

	return partida

def join_season(part):
    seasons = dict()
    for player, season, team in part:
        key = (player, team)
        if key in seasons:
            seasons[key].append(season)
        else:
            seasons[key] = [season]

    result = []
    for (player, team), season_list in seasons.items():
        season_list = sorted(map(lambda season: int(season.split("/")[0]), season_list))
        
        first = last = None
        for season in season_list:
            if first is None:
                first = last = season
            elif season - last > 1:
                result.append((player, first, last, team))
                first = last = season
            else:
                last = season
        if first is not None:
            result.append((player, first, last, team))

    return result
            
        


def gen_part_query(cnx):
    partida = set_df(cnx)
    season = []
    team = []
    player = []

    for index, p in partida.iterrows():
        for i in range(1, 12):
            if not pd.isna(p["away_player_"+str(i)]):
                season.append(p["season"])
                team.append(p["away_team_api_id"])
                player.append(int(p["away_player_"+str(i)]))
            if not pd.isna(p["home_player_"+str(i)]):
                season.append(p["season"])
                team.append(p["home_team_api_id"])
                player.append(int(p["home_player_"+str(i)]))

    part = join_season(list(dict.fromkeys(list(zip(player, season, team)))))
    
    sql_insert_part = "insert into Participacao (jogador_api_id, temporada_ini, temporada_fim, id_time) values "
    sql_part_values = "\n({},{},{},{}),"

    for i in part:
        sql_insert_part += sql_part_values.format(*i)

    sql_insert_part = sql_insert_part[:-1] + ";\n"

    return sql_insert_part


if __name__ == "__main__":
	cnx = sqlite3.connect('./database.sqlite')
	with open("dmlParticipacao.sql", "w") as file1:
		file1.write(gen_part_query(cnx))