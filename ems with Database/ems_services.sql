-- MySQL dump 10.13  Distrib 5.5.27, for Win32 (x86)
--
-- Host: 127.0.0.1    Database: ems_services
-- ------------------------------------------------------
-- Server version	5.5.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `ems_services`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `ems_services` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `ems_services`;

--
-- Table structure for table `empdetails`
--

DROP TABLE IF EXISTS `empdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empdetails` (
  `empId` int(100) NOT NULL,
  `empName` varchar(100) DEFAULT NULL,
  `empSalary` float DEFAULT NULL,
  `empAddress` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`empId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empdetails`
--

LOCK TABLES `empdetails` WRITE;
/*!40000 ALTER TABLE `empdetails` DISABLE KEYS */;
INSERT INTO `empdetails` VALUES (1,'Piyush',15000,'Mohali'),(2,'Pawan',16000,'Mohali'),(3,'Rohit',12600,'Ranchi'),(4,'Ashish',16000,'Mohali'),(5,'Gulzar',15000,'Bihar'),(6,'Yamunesh',15000,'Chandigarh'),(7,'rohan',15000,'Delhi');
/*!40000 ALTER TABLE `empdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empdetails_2`
--

DROP TABLE IF EXISTS `empdetails_2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `empdetails_2` (
  `empId` int(100) NOT NULL,
  `empName` varchar(100) DEFAULT NULL,
  `empSalary` float DEFAULT NULL,
  `empAddress` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`empId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empdetails_2`
--

LOCK TABLES `empdetails_2` WRITE;
/*!40000 ALTER TABLE `empdetails_2` DISABLE KEYS */;
INSERT INTO `empdetails_2` VALUES (1,'Piyush',15000,'Mohali'),(2,'Pawan',14000,'Mohali'),(3,'Rohit',16000,'ranchi'),(4,'Ashish',20000,'Ranchi'),(5,'Gulzar',15000,'Tangori'),(6,'Vikash',25000,'Delhi'),(7,'Basant',23000,'Noida'),(8,'Avinash',12000,'Tangori'),(234,'sfd',234,'sdf'),(654,'sdf',234,'sdf'),(12345,'fdg',3245,'sfd');
/*!40000 ALTER TABLE `empdetails_2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-03  2:22:57
