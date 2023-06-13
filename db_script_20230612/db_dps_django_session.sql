-- MySQL dump 10.13  Distrib 8.0.31, for Linux (x86_64)
--
-- Host: localhost    Database: db_dps
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0kjkwsht1dusjrh22gv770askgpd6if0','.eJyrViotTi2Kz8xLy1eyiq5WykxRsjLUAQvmJeamKlkpOWYlVirpKKXmJmbmALmJQK5DOoijl5yfC5QAkgWJeZXxIJ3GCC5Ud7hfMFBNQVF-WmZOanxBRn4J0B6InUk5iXnZegV56Uq1sbUAMCoucA:1pF6Pr:1Nvi0OgCJpf9pSQ1FRwW_A-bcQ8LMpMq-A5Fg8KbRGU','2023-01-24 04:39:15.880173'),('1pkhu1wr5jh0jzvejd1pltaglwv4j3na','.eJyrViotTi2Kz8xLy1eyiq5WykxRsjLUAQvmJeamKlkpOWYlVirpKKXmJmbmALmJQK5DOoijl5yfC5QAkgWJeZXxIJ3GCC5Ud7hfMFBNQVF-WmZOanxBRn4J0B6InUk5iXnZegV56Uq1sbUAMCoucA:1pTtZZ:EfOAMwbk2U95zY1zolMock8zNLI9ofzN9-xqdYD_i7U','2023-03-05 23:58:25.864055'),('96osgnu2ebwb8uib35p9jv4wjpon69j8','.eJyrViotTi2Kz8xLy1eyiq5WykxRsjLUAQvmJeamKlkpOWYlVirpKKXmJmbmALmJQK5DOoijl5yfC5QAkgWJeZXxIJ3GCC5Ud7hfMFBNQVF-WmZOanxBRn4J0B6InUk5iXnZegV56Uq1sbUAMCoucA:1pkN5M:oUw9qJYHY_U-Pv08oAMdjc2orMWOtO9GVvEN2-CVmqU','2023-04-20 10:43:20.570083'),('9nl6nxmrw0rw5w2hp5ny2p5jh27147fn','.eJyrViotTi2Kz8xLy1eyiq5WykxRsjLUAQvmJeamKlkpOWYlVirpKKXmJmbmALmJQK5DOoijl5yfC5QAkgWJeZXxIJ3GCC5Ud7hfMFBNQVF-WmZOanxBRn4J0B6InUk5iXnZegV56Uq1sbUAMCoucA:1peng2:2T54DG0Abn2YZWXBoaxWrx1k5tQoScRrIOOyv2nLR4I','2023-04-05 01:54:10.474641'),('k0npw6cuf82p09ptg0zf6x6f92qowgto','.eJyrViotTi2Kz8xLy1eyiq5WykxRsjLUAQvmJeamKlkpOWYlVirpKKXmJmbmALmJQK5DOoijl5yfC5QAkgWJeZXxIJ3GCC5Ud7hfMFBNQVF-WmZOanxBRn4J0B6InUk5iXnZegV56Uq1sbUAMCoucA:1q7WDB:xGr0l0HAXduWo7VQK3ZdMH6pxiE7mlzCmU5paKnT1qA','2023-06-23 07:07:05.174914');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-12  2:41:18
