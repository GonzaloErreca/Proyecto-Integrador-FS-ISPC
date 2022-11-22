-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 22-11-2022 a las 03:44:36
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `python_login`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `familia`
--

CREATE TABLE `familia` (
  `id` int(11) NOT NULL,
  `familia` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `familia`
--

INSERT INTO `familia` (`id`, `familia`) VALUES
(1, 'ACC.CONTACTORES'),
(2, 'ACC.GUARDAMOTORES'),
(3, 'ACC.INT.CAJA MOLD'),
(4, 'ACCESORIOS'),
(5, 'ARRANQUE SUAVE'),
(6, 'ART LED EXTERIOR'),
(7, 'ART.ALTA POTENCIA'),
(8, 'ARTEFACTOS PARED'),
(9, 'ARTEFACTOS SPOT'),
(10, 'BASE FUSIBLE'),
(11, 'CABLES TEXTILES'),
(12, 'CAJA MOLDEADA ELECTR'),
(13, 'CAJA MOLDEADA FIJA'),
(14, 'CONMUTADOR'),
(15, 'CONMUTADOR MOTORIZADO'),
(16, 'CONTACTORES'),
(17, 'ESTANCOS'),
(18, 'FACTOR DE POTENCIA'),
(19, 'FTE SWITCHING EXT'),
(20, 'FUENTE SWITCHING'),
(21, 'FUSIBLE'),
(22, 'GUARDAMOTORES'),
(23, 'ILUMINACION SOLAR'),
(24, 'INTECK'),
(25, 'INTECK PRECINTOS'),
(26, 'INTEK CINTAS'),
(27, 'KING LAMAPARAS'),
(28, 'LAMPARAS BULBO'),
(29, 'LAMPARAS BULBONES'),
(30, 'LAMPARAS DE MESA Y PIE'),
(31, 'LAMPARAS FILAMENTO'),
(32, 'LAMPARAS G4'),
(33, 'LAMPARAS G9'),
(34, 'LAMPARAS PAR30/38'),
(35, 'LUCES DE EMERGENCIA'),
(36, 'LUZ DE CALLE'),
(37, 'MANIOBRA Y COMANDO'),
(38, 'MULTIMEDIDOR'),
(39, 'PANELES 60X60/30X120'),
(40, 'PANELES 6W A 24W'),
(41, 'PANELES COB'),
(42, 'PANELES GRAN FORMATO'),
(43, 'PERFILES PVC'),
(44, 'PORTA LAMPARAS'),
(45, 'PROLONGADORES'),
(46, 'R.TERMICO-CONTACTOR'),
(47, 'REFLECTORES'),
(48, 'REFLECTORES PRO'),
(49, 'RELE AUXILIAR'),
(50, 'RELE ELECTRONICO'),
(51, 'RIEL DIN - ACCESORIO'),
(52, 'RIEL DIN - CONTACTOR'),
(53, 'RIEL DIN - DISYUNTOR'),
(54, 'RIEL DIN-DESCARGADOR'),
(55, 'RIEL DIN-SECCIONADOR'),
(56, 'RIEL DIN-TERMICAS 10'),
(57, 'RIEL DIN-TERMICAS 6'),
(58, 'RIEL DIN-TERMICAS DC'),
(59, 'SECCIONADOR'),
(60, 'SECCIONADOR FUSIBLE'),
(61, 'SMART'),
(62, 'SOLAR'),
(63, 'SPOT AR111'),
(64, 'SPOT LIGHT DICRO'),
(65, 'TIRA DE LED 2216'),
(66, 'TIRA DE LED 2835'),
(67, 'TIRA DE LED 3528'),
(68, 'TIRA DE LED 5050'),
(69, 'TIRA DE LED 5050 24V'),
(70, 'TRANSFERENCIA AUTO'),
(71, 'TUBO DE LED'),
(72, 'VARIADOR DE VELOCIDAD');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marca`
--

CREATE TABLE `marca` (
  `id` int(11) NOT NULL,
  `marca` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `marca`
--

INSERT INTO `marca` (`id`, `marca`) VALUES
(1, 'CHINT'),
(2, 'INTECK'),
(3, 'KING'),
(4, 'MACROLED'),
(5, 'POWERSWITCH');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `productos`
--

CREATE TABLE `productos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(500) NOT NULL,
  `descripcion` varchar(500) NOT NULL,
  `precio` double(10,2) NOT NULL,
  `stock` int(255) NOT NULL,
  `foto` varchar(1000) NOT NULL,
  `marca_id` int(11) NOT NULL,
  `familia_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` smallint(3) UNSIGNED NOT NULL,
  `username` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `password` char(102) COLLATE utf8_unicode_ci NOT NULL,
  `fullname` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`) VALUES
(1, 'admin', 'pbkdf2:sha256:260000$Om11MxI3GKizxNO8$376b471808215690a7c07efaf0e08f573b0f9032a64ed8930c9e26aab29f9c80', 'admin');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `familia`
--
ALTER TABLE `familia`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `marca`
--
ALTER TABLE `marca`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `productos`
--
ALTER TABLE `productos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `marca_fk` (`marca_id`),
  ADD KEY `familia_fk` (`familia_id`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `familia`
--
ALTER TABLE `familia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT de la tabla `marca`
--
ALTER TABLE `marca`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `productos`
--
ALTER TABLE `productos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` smallint(3) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `productos`
--
ALTER TABLE `productos`
  ADD CONSTRAINT `familia_fk` FOREIGN KEY (`familia_id`) REFERENCES `familia` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `marca_fk` FOREIGN KEY (`marca_id`) REFERENCES `marca` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
