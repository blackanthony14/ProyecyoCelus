-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 08, 2021 at 08:53 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `basesnormales`
--

-- --------------------------------------------------------

--
-- Table structure for table `pokemones`
--

DROP TABLE IF EXISTS `pokemones`;
CREATE TABLE IF NOT EXISTS `pokemones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  `elemnto` varchar(128) NOT NULL,
  `hp` int(11) NOT NULL,
  `atk` int(11) NOT NULL,
  `deff` int(11) NOT NULL,
  `description` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pokemones`
--

INSERT INTO `pokemones` (`id`, `name`, `elemnto`, `hp`, `atk`, `deff`, `description`) VALUES
(1, 'Bulbasauur', 'Planta y Veneno', 45, 49, 49, 'Pokemon que se puede escoger de manera inicial en la region de Kanto.'),
(2, 'Ivysaur', 'Planta y Veneno', 60, 62, 63, 'Evolucion del pokemon Bulbasaur'),
(3, 'Venusaur', 'Planta y Veneno', 80, 82, 83, 'Evolucion del pokemon Ivysaur, puede acceder a su mega-evolucion'),
(4, 'Charmander', 'Fuego', 39, 52, 43, 'Pokemon que se puede escoger de manera inicial en la region de Kanto.'),
(5, 'Charmeleon', 'Fuego', 58, 64, 58, 'Este es la evolucion de Charmander'),
(6, 'Charizard', 'Fuego y volador', 78, 84, 78, 'Este es la evolucion de Charmeleon, puede acceder a su mega-evolucion'),
(7, 'Squirtle', 'Agua', 44, 48, 45, 'Pokemon que se puede escoger de manera inicial en la region de Kanto.'),
(8, 'Wartortle', 'Agua', 59, 63, 80, 'Evolucion del pokemon Squirtle'),
(9, 'Blastoise', 'Agua', 79, 83, 100, 'Evolucion del pokemon Wartortle, puede acceder a su mega-evolucion');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
