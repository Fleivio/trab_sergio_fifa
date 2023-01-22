-- Selecionar o time que mais venceu partidas;

select * from Time join
(select count(*) as vitorias, (case
           when gois_time_da_casa > gois_time_convidado then time_da_casa_id
           when gois_time_convidado > gois_time_da_casa then time_convidado_id
   end) as vencedor
from Partida where gois_time_convidado <> gois_time_da_casa
group by vencedor) vitorias on id_time = vitorias.vencedor order by vitorias.vitorias desc
limit 1;


-- Selecionar a quantidade de clubes em que o jogador mais velho já atuou

select count(Participacao.id_participacao) as Times, jogador_mais_velho.*
from Participacao
        natural join
        (select * from Jogador order by data_nascimento limit 1) jogador_mais_velho
group by jogador_mais_velho.jogador_api_id;


-- Qual jogador mais trocou de clube

select nome
from Jogador
       natural join Participacao
group by jogador_api_id
order by count(*) desc
limit 1;
