-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 28, 2021 at 05:04 PM
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
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `transacciones`
--

INSERT INTO `transacciones` (`id`, `user_id`, `telefono_id`) VALUES
(1, 1, 1),
(2, 1, 1),
(3, 1, 1),
(4, 1, 1),
(5, 1, 2);

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
  PRIMARY KEY (`id`),
  UNIQUE KEY `public_id` (`public_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `public_id`, `name`, `password`, `admin`) VALUES
(1, '6f7debe5-0d15-4897-8208-1308108590d9', 'admin', 'sha256$zcv2RfQcXarm0WU1$7c6def35cede261015e65ed2bd56ad0c0d19de4366000128540df5f9c9988911', 1),
(2, 'b84e9129-3d82-4cab-81a4-c08c6f818683', 'Anthony', 'sha256$jzI1AvCEYtQPK0T4$e85d2ce4e43a954486b508a380ee34fcd62f52888241d7f89bbeaa12684220a0', 1),
(3, '8e06bb88-3ab4-467b-a325-665561e1bed6', 'Paul', 'sha256$hFr2PsmQw0GQn9LD$6fda45f47e89fe685803d378022abddb72ed87265bbb09b69207a371c865f2c1', 0);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
