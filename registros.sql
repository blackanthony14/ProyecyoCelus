-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 15, 2021 at 04:30 PM
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
-- Database: `registros`
--

-- --------------------------------------------------------

--
-- Table structure for table `empleado`
--

DROP TABLE IF EXISTS `empleado`;
CREATE TABLE IF NOT EXISTS `empleado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `codigoId` varchar(200) NOT NULL,
  `puesto` varchar(200) NOT NULL,
  `rol` varchar(200) DEFAULT NULL,
  `fotografia` varchar(500) DEFAULT NULL,
  `descripcion` varchar(500) DEFAULT NULL,
  `anotacionE` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `empleado`
--

INSERT INTO `empleado` (`id`, `nombre`, `codigoId`, `puesto`, `rol`, `fotografia`, `descripcion`, `anotacionE`) VALUES
(1, 'Anthony Duffis Newball', '801170158', 'Ascesor de Ingenieria', 'Otorgar el conocimiento a los nuevos empleados.', 'https://definicion.mx/wp-content/uploads/2013/06/maestro.jpg', '21 years, capaz de de trabajar bajo presion, apto para el trabajo en equipo.', 'Besto trabajador');

-- --------------------------------------------------------

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
CREATE TABLE IF NOT EXISTS `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `codigoId` varchar(200) NOT NULL,
  `precio` int(11) NOT NULL,
  `categoria` varchar(200) DEFAULT NULL,
  `fotografiaLink` varchar(500) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `anotacionG` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `item`
--

INSERT INTO `item` (`id`, `nombre`, `codigoId`, `precio`, `categoria`, `fotografiaLink`, `description`, `anotacionG`) VALUES
(1, 'Laptop HP', '334689', 250000, 'Electronica', 'https://icdn.dtcn.com/image/digitaltrends_es/dell-xps-13-9310-featured-image-2-768x768.jpg', 'Procesador Intel Core i3-1005G1 de 10ª generación, 8 GB de RAM y 256 GB de almacenamiento en disco de estado sólido PCIe NVMe.', 'Buena Laptop');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
