-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 28, 2021 at 06:06 PM
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
-- Database: `ventadecelus`
--

-- --------------------------------------------------------

--
-- Table structure for table `telefono`
--

DROP TABLE IF EXISTS `telefono`;
CREATE TABLE IF NOT EXISTS `telefono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `marca` varchar(200) NOT NULL,
  `imei` varchar(200) NOT NULL,
  `precio` int(11) NOT NULL,
  `ram` varchar(100) NOT NULL,
  `pantalla` varchar(100) NOT NULL,
  `gama` varchar(100) NOT NULL,
  `sistemaOperativo` varchar(200) NOT NULL,
  `espacionAlma` varchar(100) DEFAULT NULL,
  `aviable` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `telefono`
--

INSERT INTO `telefono` (`id`, `nombre`, `marca`, `imei`, `precio`, `ram`, `pantalla`, `gama`, `sistemaOperativo`, `espacionAlma`, `aviable`) VALUES
(1, 'Apple', 'Iphone 11', '567778970248001', 330000, '8gb', '6.06 pulgadas', 'Pro', 'iOS', '128gb', 1),
(2, 'Samsung', 'Galaxy', '355818956401380', 350000, '16gb', '6.8 inches', 'S21', 'Android 11', '256gb', 1),
(3, 'Apple', 'Iphone 12', '567778972457001', 450000, '16gb', '6.06 pulgadas', 'Ultra', 'iOS', '256gb', 1),
(4, 'Samsung', 'Galaxy', '980239544211269', 635000, '32gb', '6.8 inches', 'S21 Pro', 'Android 11', '500gb', 1),
(5, 'Samsung', 'Galaxy', '987862871378642', 120000, '4gb', '5.7 inches', 'A10', 'Android 8', '16gb', 1),
(6, 'Huawei', 'Huawei', '865442155621418', 367000, '6GB', '6.1 inches', 'P40', 'Android 10', '128GB', 1),
(7, 'Huawei', 'Huawei', '504697812285041', 377000, '6GB', '6.1 inches', 'P40', 'Android 10', '200GB', 1),
(8, 'Samsung', 'Galaxy', '454451230041580', 470000, '16gb', '6.8 inches', 'S20', 'Android 10', '200GB', 1);

-- --------------------------------------------------------

--
-- Table structure for table `transacciones`
--

DROP TABLE IF EXISTS `transacciones`;
CREATE TABLE IF NOT EXISTS `transacciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `telefono_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `public_id` varchar(100) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `admin` tinyint(1) DEFAULT NULL,
  `recoverPass` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `public_id` (`public_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `public_id`, `name`, `password`, `admin`, `recoverPass`) VALUES
(1, 'cb94e99f-a664-4bb1-ab0e-d270d65b2c61', 'Paul', 'sha256$mgnxydUCqXojo9cn$5e0a3dfd31e5191b1d29b5af9c470cc10c99f230093ec7a7e9ee366e1710fe96', 0, '12345'),
(2, '215391b6-6b05-41e2-8216-830e788bc6ab', 'Anthony', 'sha256$3GOKXTG3gSY2TwV1$bb03bdf4cc80409ee6dd628d2ef940cdfb84d6c9864814a180ccfd9b6cf77ef1', 1, '12345');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
