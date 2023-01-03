drop database if exists `trabSergio`;
CREATE DATABASE  IF NOT EXISTS `trabSergio`;
USE `trabSergio`;

DROP TABLE IF EXISTS `Jogador`;
CREATE TABLE `Jogador` (
  `jogador_api_id` int,
  `nome` varchar(20),
  `data_nascimento` datetime,
  PRIMARY KEY (`jogador_api_id`)
)

drop table if exists `Participacao`;
create table `Participacao`(
    `jogador_api_id` int,
    `data` datetime,
    `id_time` int,
    primary key (`jogador_api_id`, `data`)
    constraint foreign key (`jogador_api_id`) references `Jogador` (`jogador_api_id`),
    constraint foreign key (`id_time`) references `Time` (`id_time`)
)

DROP TABLE IF EXISTS `Time`;
CREATE TABLE `Time` (
    `id_time` int,
    `time_nome` varchar(20),
    `time_sigla` varchar(10),
    primary key (`id_time`)
)