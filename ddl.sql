drop database if exists `trabSergio`;
CREATE DATABASE  IF NOT EXISTS `trabSergio`;
USE `trabSergio`;

DROP TABLE IF EXISTS `Jogador`;
CREATE TABLE `Jogador` (
  `jogador_api_id` int,
  `nome` varchar(50),
  `data_nascimento` datetime,
  PRIMARY KEY (`jogador_api_id`)
);

DROP TABLE IF EXISTS `Time`;
CREATE TABLE `Time` (
    `id_time` int,
    `time_nome` varchar(50),
    `time_sigla` varchar(10),
    primary key (`id_time`)
);

drop table if exists `Participacao`;
create table `Participacao`(
    `jogador_api_id` int,
    `temporada` varchar(10),
    `id_time` int,
    primary key (`jogador_api_id`, `temporada`, `id_time`),
    foreign key (`jogador_api_id`) references `Jogador` (`jogador_api_id`),
    foreign key (`id_time`) references `Time` (`id_time`)
);
