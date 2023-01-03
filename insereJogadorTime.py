import sqlite3
import pandas as pd

cnx = sqlite3.connect('./database.sqlite')


def gen_insert_query(df, values_format):
    result = ""
    for i in range(0, len(df)):
        line = df.values[i]
        result += values_format.format(*line)

    return result[:-1] + ';'


def gen_player_query():
    player_query = "SELECT player_api_id, player_name, birthday FROM Player"

    df = pd.read_sql_query(player_query, cnx)

    sql_insert_player = "insert into Jogador (jogador_api_id, nome, data_nascimento) values "
    sql_player_values = "\n({},\"{}\",\"{}\"),"

    sql_insert_player += gen_insert_query(df, sql_player_values)

    return sql_insert_player


def gen_team_query():
    team_query = "SELECT team_api_id, team_long_name, team_short_name FROM Team"

    df = pd.read_sql_query(team_query, cnx)

    sql_insert_team = "insert into Time (id_time, time_nome, time_sigla) values "
    sql_team_values = "\n({},\"{}\",\"{}\"),"

    sql_insert_team += gen_insert_query(df, sql_team_values)

    return sql_insert_team


with open("insere.sql", "w") as sql_insere:
    sql_insere.write(gen_team_query())
    sql_insere.write("\n" * 10)
    sql_insere.write(gen_player_query())
