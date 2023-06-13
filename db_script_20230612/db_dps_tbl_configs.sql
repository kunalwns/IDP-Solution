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
-- Table structure for table `tbl_configs`
--

DROP TABLE IF EXISTS `tbl_configs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_configs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `config_uuid` varchar(45) DEFAULT NULL,
  `config_name` varchar(45) DEFAULT NULL,
  `display_name` varchar(45) DEFAULT NULL,
  `default_configuration` varchar(45) DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `company_id` int DEFAULT NULL,
  `status` int DEFAULT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_configs`
--

LOCK TABLES `tbl_configs` WRITE;
/*!40000 ALTER TABLE `tbl_configs` DISABLE KEYS */;
INSERT INTO `tbl_configs` VALUES (1,'2eee322e-ee27-11ed-a674-f701c6b8ba4d','Healthcare','Healthcare',NULL,1,3,1,'2023-05-09 05:05:57'),(2,'8817edb4-ee35-11ed-a674-f701c6b8ba4d','Medical Report','Medical Report',NULL,1,3,1,'2023-05-09 06:48:40'),(3,'f8189c14-ef8c-11ed-aa9c-8d4f9ad018d7','Medical Domain','Medical Domain',NULL,1,3,1,'2023-05-10 23:47:05'),(18,'152a535a-f065-11ed-aa9c-8d4f9ad018d7','Claim domain','Claim domain',NULL,1,3,0,'2023-05-12 01:34:05'),(19,'b1bc3df4-f07a-11ed-aa9c-8d4f9ad018d7','Demo','Demo',NULL,1,3,0,'2023-05-12 04:08:47'),(20,'a231f77e-f2e2-11ed-aa9c-8d4f9ad018d7','Demo Use case','Demo Use case',NULL,1,3,1,'2023-05-15 05:37:51'),(21,'0b55dca2-f47d-11ed-b5bb-63e9c34ee15e','AIML DEMO','AIML DEMO',NULL,1,3,1,'2023-05-17 06:35:41'),(22,'b9abf286-f93d-11ed-a60f-15faed2414d8','demo test','demo test',NULL,1,3,1,'2023-05-23 07:45:02'),(23,'8fd627f2-fa09-11ed-a60f-15faed2414d8','Generative ai demo','Generative ai demo',NULL,1,3,1,'2023-05-24 08:04:09'),(24,'a8717982-fa0f-11ed-a60f-15faed2414d8','demo AI','demo AI',NULL,1,3,1,'2023-05-24 08:47:47'),(25,'e2162d66-facf-11ed-a60f-15faed2414d8','GenAI DEmo','GenAI DEmo',NULL,1,3,1,'2023-05-25 07:43:47'),(26,'08ed7d88-fec0-11ed-886c-c5d939dd003f','Genai','Genai',NULL,1,3,1,'2023-05-30 08:00:25'),(27,'0d9b5500-0378-11ee-918f-910fd4c6cba1','Invoice_sol','Invoice_sol',NULL,1,3,1,'2023-06-05 08:07:45');
/*!40000 ALTER TABLE `tbl_configs` ENABLE KEYS */;
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
