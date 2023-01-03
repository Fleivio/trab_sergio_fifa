import sqlite3
import pandas as pd

cnx = sqlite3.connect('./database.sqlite')
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

part = list(zip(player, season, team))

sql_insert_part = "insert into Participacao (jogador_api_id, temporada, id_time) values "
sql_part_values = "\n({},\"{}\",{}),"

for i in part:
	sql_insert_part += sql_part_values.format(*i)

with open("inserePart.sql", "w") as file1:
	file1.write(sql_insert_part)


