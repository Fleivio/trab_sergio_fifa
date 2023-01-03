import sqlite3
import pandas as pd

cnx = sqlite3.connect('./database.sqlite')

# Criação dos dataframes
jogador = pd.read_sql_query("SELECT * FROM Player", cnx)
time = pd.read_sql_query("SELECT * FROM Team", cnx)
partida = pd.read_sql_query("SELECT * FROM Match", cnx)

# Deletando colunas que não vão ser utilizadas
jogador = jogador.drop("id", axis=1)
jogador = jogador.drop("player_fifa_api_id", axis=1)

time = time.drop("id", axis=1)
time = time.drop("team_fifa_api_id", axis=1)

for i in range (1,12):
  partida = partida.drop("home_player_X" + str(i), axis=1)
  partida = partida.drop("home_player_Y" + str(i), axis=1)
  partida = partida.drop("away_player_X" + str(i), axis=1)
  partida = partida.drop("away_player_Y" + str(i), axis=1)

columns = ["goal","shoton","shotoff","foulcommit","card","cross","corner","possession","id","B365H","B365D","B365A","BWH","BWD","BWA","IWH","IWD","IWA","LBH","LBD","LBA","PSH","PSD","PSA","WHH","WHD","WHA","SJH","SJD","SJA","VCH","VCD","VCA","GBH","GBD","GBA","BSH","BSD","BSA"]

for column in columns:
  partida = partida.drop(column, axis=1)


# Criação do dataframe de participacao
part = ({'season': ["a"], 'team_id': [0], 'player_id': [0]})
participacao = pd.DataFrame(part)

# Insere os jogadores no df de participação ** demora muito pra executar, provavelmente da pra otimizar isso kkk
for index, p in partida.iterrows():
  if(not pd.isna(p["away_player_1"])):
    for i in range(1,12):
      row1 = {"season": p["season"], "team_id": p["home_team_api_id"], "player_id": p["home_player_"+str(i)]}
      row2 = {"season": p["season"], "team_id": p["away_team_api_id"], "player_id": p["away_player_"+str(i)]}
      participacao = participacao.append(row1, ignore_index=True)
      participacao = participacao.append(row2, ignore_index=True)

participacao = participacao.drop(0, axis=0)
    

