import sqlite3
import pandas as pd

def gen_match_query(cnx):
    sql_insert_partida = "INSERT INTO Partida ( time_da_casa_id, time_convidado_id, gois_time_da_casa, gois_time_convidado, `data`, temporada) values "
    sql_values = "\n({}, {}, {}, {}, \"{}\", {}),"

    query = "select home_team_api_id, away_team_api_id, home_team_goal, away_team_goal, date, season from Match"

    df = pd.read_sql_query(query, cnx)
    df["season"] = df["season"].map(lambda season: int(season.split("/")[0]))

    for i in range(len(df)):
        sql_insert_partida += sql_values.format(*(df.values[i]))
    sql_insert_partida = sql_insert_partida[:-1] + ";\n"

    return sql_insert_partida

if __name__ == "__main__":
    cnx = sqlite3.connect('./database.sqlite')
    with open("dmlPartida.sql", "w") as file1:
        file1.write(gen_match_query(cnx))