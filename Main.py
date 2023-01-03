from insereJogadorTime import gen_team_query, gen_player_query
from insereParticipacao import gen_part_query
from inserePartida import gen_match_query

import sqlite3

cnx = sqlite3.connect('./database.sqlite')

with open("dml.sql", "w") as file1:
    file1.write(gen_team_query(cnx))
    file1.write(gen_player_query(cnx))
    file1.write(gen_part_query(cnx))
    file1.write(gen_match_query(cnx))