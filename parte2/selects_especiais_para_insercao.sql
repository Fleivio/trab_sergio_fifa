select idClube, id_time
from jogadores_mais_valiosos.clube c
         join
     trabfdb.time t on nomeClube like time_sigla
         or nomeClube like concat('%', time_nome, '%')
         or time_nome like concat('%', nomeClube, '%');



insert into time (id_time, time_nome, time_sigla)
SELECT *
from trabfdb.time
union
select idClube, nomeClube, null
from jogadores_mais_valiosos.clube
where idClube <> 59
  and idClube not in (select idClube
                      from jogadores_mais_valiosos.clube,
                           trabfdb.time t
                      where nomeClube like time_sigla
                         or nomeClube like concat('%', time_nome, '%')
                         or time_nome like concat('%', nomeClube, '%'));




insert into jogador (jogador_api_id, nome, data_nascimento, nacionalidade, altura, peso)
    (SELECT jogador_api_id, nome, data_nascimento, NULL, altura, peso
     from trabfdb.jogador)
union
(select rankJog, nomeJog, timestampadd(year, -idade, '2022-01-01'), nacionalidade, NULL, NULL
 from jogadores_mais_valiosos.jogador
 where jogador.rankJog not in (1, 12, 18, 19, 20, 21, 22, 30, 31));

insert into partida (time_da_casa_id, time_convidado_id, gois_time_da_casa, gois_time_convidado, data, temporada)
SELECT *
from trabfdb.partida;

insert into valor_jogador (jogador_api_id, temporada_ini, temporada_fim, valor_euros)
SELECT (
           case
               when rankJog = 1 then 701154
               when rankJog = 12 then 194165
               when rankJog = 18 then 704523
               when rankJog = 19 then 488139
               when rankJog = 20 then 460632
               when rankJog = 21 then 292462
               when rankJog = 22 then 169200
               when rankJog = 30 then 422685
               when rankJog = 31 then 19533
               else rankJog
               end
           ),
       2023,
       2023,
       valorJog_Mi_Euros * 1000000
from jogadores_mais_valiosos.jogador;

insert into participacao (jogador_api_id, temporada_ini, temporada_fim, id_time)
select jogador_api_id, temporada_ini, temporada_fim, id_time
from trabfdb.participacao
union
select (case
            when rankJog = 1 then 701154
            when rankJog = 12 then 194165
            when rankJog = 18 then 704523
            when rankJog = 19 then 488139
            when rankJog = 20 then 460632
            when rankJog = 21 then 292462
            when rankJog = 22 then 169200
            when rankJog = 30 then 422685
            when rankJog = 31 then 19533
            else rankJog
    end),
       null,
       null,
       (
           case
               when idClube = 59 then 8178
               when idClube = 53 then 6269
               when idClube = 20 then 8197
               when idClube = 52 then 8277
               when idClube = 39 then 8455
               when idClube = 5 then 8456
               when idClube = 60 then 8528
               when idClube = 30 then 8535
               when idClube = 23 then 8564
               when idClube = 18 then 8586
               when idClube = 43 then 8593
               when idClube = 54 then 8600
               when idClube = 9 then 8633
               when idClube = 10 then 8634
               when idClube = 49 then 8636
               when idClube = 22 then 8639
               when idClube = 37 then 8650
               when idClube = 26 then 8654
               when idClube = 11 then 8658
               when idClube = 36 then 8686
               when idClube = 48 then 8696
               when idClube = 41 then 8721
               when idClube = 21 then 9768
               when idClube = 33 then 9772
               when idClube = 47 then 9773
               when idClube = 14 then 9783
               when idClube = 4 then 9789
               when idClube = 12 then 9823
               when idClube = 15 then 9825
               when idClube = 24 then 9827
               when idClube = 6 then 9829
               when idClube = 7 then 9847
               when idClube = 19 then 9850
               when idClube = 58 then 9865
               when idClube = 14 then 9868
               when idClube = 21 then 9869
               when idClube = 55 then 9882
               when idClube = 31 then 9885
               when idClube = 28 then 9906
               when idClube = 56 then 9931
               when idClube = 21 then 9986
               when idClube = 38 then 9987
               when idClube = 21 then 9994
               when idClube = 27 then 10205
               when idClube = 44 then 10260
               when idClube = 34 then 10269
               else idClube
               end
           )
from jogadores_mais_valiosos.jogou;

insert into time_liga (idLiga, id_time) select idLiga,
                                            (
           case
               when idClube = 59 then 8178
               when idClube = 53 then 6269
               when idClube = 20 then 8197
               when idClube = 52 then 8277
               when idClube = 39 then 8455
               when idClube = 5 then 8456
               when idClube = 60 then 8528
               when idClube = 30 then 8535
               when idClube = 23 then 8564
               when idClube = 18 then 8586
               when idClube = 43 then 8593
               when idClube = 54 then 8600
               when idClube = 9 then 8633
               when idClube = 10 then 8634
               when idClube = 49 then 8636
               when idClube = 22 then 8639
               when idClube = 37 then 8650
               when idClube = 26 then 8654
               when idClube = 11 then 8658
               when idClube = 36 then 8686
               when idClube = 48 then 8696
               when idClube = 41 then 8721
               when idClube = 21 then 9768
               when idClube = 33 then 9772
               when idClube = 47 then 9773
               when idClube = 14 then 9783
               when idClube = 4 then 9789
               when idClube = 12 then 9823
               when idClube = 15 then 9825
               when idClube = 24 then 9827
               when idClube = 6 then 9829
               when idClube = 7 then 9847
               when idClube = 19 then 9850
               when idClube = 58 then 9865
               when idClube = 14 then 9868
               when idClube = 21 then 9869
               when idClube = 55 then 9882
               when idClube = 31 then 9885
               when idClube = 28 then 9906
               when idClube = 56 then 9931
               when idClube = 21 then 9986
               when idClube = 38 then 9987
               when idClube = 21 then 9994
               when idClube = 27 then 10205
               when idClube = 44 then 10260
               when idClube = 34 then 10269
               else idClube
               end
           )
                                            from jogadores_mais_valiosos.participa;


update jogador join jogadores_mais_valiosos.jogador on jogador_api_id = rankJog
set data_nascimento = timestampadd(year, -idade, '2022-01-01')
where jogador.jogador_api_id < 1000;

select * from jogador join jogadores_mais_valiosos.jogador on jogador_api_id = rankJog