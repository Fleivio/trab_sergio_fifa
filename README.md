# trab_sergio_fifa

Armazena informações sobre jogadores, times de futebol, suas relações e partidas do campeonato europeu, entre os anos de 2009 e 2016. 


## Para jogadores, armazena-se:
- seu nome
- sua data de nascimento
- seu id
- sua altura
- seu peso

## Para times, armazena-se
- seu id
- seu nome
- sua sigla

## Para partida, armazena-se
- o time da casa
- o time convidado
- gois do time da casa
- gois do time convidado
- data
- temporada

Além dessas três tabelas, é necessário uma para manter o relacionamento entre jogadores e seus times. 

## A tabela Participacao armazena
- id do jogador
- id do time
- temporada em que o jogador esteve no time


Fonte utilizada (https://www.kaggle.com/datasets/hugomathien/soccer)