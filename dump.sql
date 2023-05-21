CREATE DATABASE  IF NOT EXISTS `db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db`;
-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: db
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `викладачі`
--

DROP TABLE IF EXISTS `викладачі`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `викладачі` (
  `idвикладачі` int NOT NULL AUTO_INCREMENT,
  `прізвище` varchar(45) DEFAULT NULL,
  `імя` varchar(45) DEFAULT NULL,
  `по_батькові` varchar(50) DEFAULT NULL,
  `дата_народження` date DEFAULT NULL,
  `idкафедри` int DEFAULT NULL,
  `посада` varchar(50) DEFAULT NULL,
  `курс` varchar(70) DEFAULT NULL,
  `телефон` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`idвикладачі`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `викладачі`
--

LOCK TABLES `викладачі` WRITE;
/*!40000 ALTER TABLE `викладачі` DISABLE KEYS */;
INSERT INTO `викладачі` VALUES (7,'Михайло','Махно ','Федорович','2000-01-01',1,'асистент','комп\'ютерні мережі','12345678'),(8,'Юлія','Шевчук','Володимирівна','2000-01-01',1,'асистент','архітектура обчислювальних систем','12345678');
/*!40000 ALTER TABLE `викладачі` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `кафедри`
--

DROP TABLE IF EXISTS `кафедри`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `кафедри` (
  `idкафедри` int NOT NULL AUTO_INCREMENT,
  `назва_кафедри` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`idкафедри`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `кафедри`
--

LOCK TABLES `кафедри` WRITE;
/*!40000 ALTER TABLE `кафедри` DISABLE KEYS */;
INSERT INTO `кафедри` VALUES (1,'кафедра системного аналізу та теорії прийняття рішень'),(2,'кафедра прикладної статистики');
/*!40000 ALTER TABLE `кафедри` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'db'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-21 15:56:27
