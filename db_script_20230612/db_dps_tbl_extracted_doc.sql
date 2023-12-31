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
-- Table structure for table `tbl_extracted_doc`
--

DROP TABLE IF EXISTS `tbl_extracted_doc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_extracted_doc` (
  `id` int NOT NULL AUTO_INCREMENT,
  `doc_id` int DEFAULT NULL COMMENT '\n\n\n\n',
  `page_no` varchar(200) DEFAULT NULL,
  `extracted_json_location` varchar(500) DEFAULT NULL,
  `extracted_table_json_location` varchar(500) DEFAULT NULL,
  `process_start_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `process_end_time` datetime DEFAULT CURRENT_TIMESTAMP,
  `status` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_extracted_doc`
--

LOCK TABLES `tbl_extracted_doc` WRITE;
/*!40000 ALTER TABLE `tbl_extracted_doc` DISABLE KEYS */;
INSERT INTO `tbl_extracted_doc` VALUES (1,12,'page_1','{}','{}','2023-05-12 00:46:24','2023-05-12 00:46:24',3),(2,13,'page_1','{}','{}','2023-05-12 07:46:46','2023-05-12 07:46:46',3),(3,14,'page_1','{}','{}','2023-05-16 02:01:48','2023-05-16 02:01:48',3),(4,16,'claim_15','{}','{}','2023-05-17 02:27:02','2023-05-17 02:27:02',3),(5,17,'page_1','{}','{}','2023-05-17 02:37:02','2023-05-17 02:37:02',3),(6,18,'page_2','{}','{}','2023-05-17 03:51:22','2023-05-17 03:51:22',3),(7,18,'page_1','{}','{}','2023-05-17 03:51:32','2023-05-17 03:51:32',3),(8,18,'page_4','{}','{}','2023-05-17 03:51:45','2023-05-17 03:51:45',3),(9,18,'page_6','{}','{}','2023-05-17 03:51:56','2023-05-17 03:51:56',3),(10,18,'page_8','{}','{}','2023-05-17 03:52:08','2023-05-17 03:52:08',3),(11,18,'page_5','{}','{}','2023-05-17 03:52:23','2023-05-17 03:52:23',3),(12,18,'page_7','{}','{}','2023-05-17 03:52:35','2023-05-17 03:52:35',3),(13,18,'page_3','{}','{}','2023-05-17 03:52:49','2023-05-17 03:52:49',3),(14,18,'page_10','{}','{}','2023-05-17 03:53:04','2023-05-17 03:53:04',3),(15,18,'page_9','{}','{}','2023-05-17 03:53:19','2023-05-17 03:53:19',3),(16,19,'page_1','{}','{}','2023-05-23 02:15:22','2023-05-23 02:15:22',3),(17,20,'page_2','{}','{}','2023-05-23 03:53:20','2023-05-23 03:53:20',3),(18,20,'page_1','{}','{}','2023-05-23 03:53:41','2023-05-23 03:53:41',3),(19,21,'page_1','{}','{}','2023-05-23 06:17:30','2023-05-23 06:17:30',4),(20,22,'page_1','{}','{}','2023-05-23 06:18:36','2023-05-23 06:18:36',4),(21,15,'claim_15','{}','{}','2023-05-23 06:34:05','2023-05-23 06:34:05',4),(22,23,'page_1','{}','{}','2023-05-23 06:35:12','2023-05-23 06:35:12',4),(23,22,'page_1','{}','{}','2023-05-23 22:55:20','2023-05-23 22:55:20',4),(24,24,'page_1','{}','{}','2023-05-23 23:52:11','2023-05-23 23:52:11',4),(25,23,'page_1','{}','{}','2023-05-23 23:53:06','2023-05-23 23:53:06',4),(26,24,'page_1','{}','{}','2023-05-24 01:10:06','2023-05-24 01:10:06',4),(27,25,'page_1','{}','{}','2023-05-24 01:11:10','2023-05-24 01:11:10',4),(28,22,'page_1','{}','{}','2023-05-24 01:12:26','2023-05-24 01:12:26',4),(29,26,'claim_8','{}','{}','2023-05-24 01:16:41','2023-05-24 01:16:41',4),(30,27,'page_1','{}','{}','2023-05-24 04:05:07','2023-05-24 04:05:07',4),(31,28,'page_1','{}','{}','2023-05-24 04:48:30','2023-05-24 04:48:30',4),(32,28,'page_1','{}','{}','2023-05-24 23:47:25','2023-05-24 23:47:25',3),(33,28,'page_1','{}','{}','2023-05-24 23:49:44','2023-05-24 23:49:44',3),(34,28,'page_1','{}','{}','2023-05-24 23:52:38','2023-05-24 23:52:38',3),(35,28,'page_1','{}','{}','2023-05-24 23:55:35','2023-05-24 23:55:35',3),(36,28,'page_1','{}','{}','2023-05-24 23:57:26','2023-05-24 23:57:26',3),(37,23,'page_1','{}','{}','2023-05-24 23:58:51','2023-05-24 23:58:51',3),(38,25,'page_1','{}','{}','2023-05-25 00:01:28','2023-05-25 00:01:28',3),(39,26,'claim_8','{}','{}','2023-05-25 00:03:05','2023-05-25 00:03:05',3),(40,26,'claim_8','{}','{}','2023-05-25 00:05:59','2023-05-25 00:05:59',3),(41,22,'page_1','{}','{}','2023-05-25 00:17:42','2023-05-25 00:17:42',3),(42,24,'page_1','{}','{}','2023-05-25 00:18:29','2023-05-25 00:18:29',3),(43,25,'page_1','{}','{}','2023-05-25 01:31:37','2023-05-25 01:31:37',3),(44,27,'page_1','{}','{}','2023-05-25 01:36:08','2023-05-25 01:36:08',4),(45,20,'page_2','{}','{}','2023-05-25 01:37:21','2023-05-25 01:37:21',4),(46,20,'page_1','{}','{}','2023-05-25 01:37:21','2023-05-25 01:37:21',4),(47,21,'page_1','{}','{}','2023-05-25 01:38:45','2023-05-25 01:38:45',4),(48,28,'page_1','{}','{}','2023-05-25 01:40:04','2023-05-25 01:40:04',4),(49,29,'page_1','{}','{}','2023-05-25 01:41:26','2023-05-25 01:41:26',4),(50,22,'page_1','{}','{}','2023-05-25 01:43:14','2023-05-25 01:43:14',3),(51,23,'page_1','{}','{}','2023-05-25 02:04:14','2023-05-25 02:04:14',3),(52,25,'page_1','{}','{}','2023-05-25 02:12:13','2023-05-25 02:12:13',3),(53,27,'page_1','{}','{}','2023-05-25 02:14:52','2023-05-25 02:14:52',4),(54,26,'claim_8','{}','{}','2023-05-25 02:18:16','2023-05-25 02:18:16',4),(55,29,'page_1','{}','{}','2023-05-25 02:24:30','2023-05-25 02:24:30',4),(56,29,'page_1','{}','{}','2023-05-25 02:29:47','2023-05-25 02:29:47',4),(57,28,'page_1','{}','{}','2023-05-25 03:32:56','2023-05-25 03:32:56',4),(58,30,'page_1','{}','{}','2023-05-25 03:44:41','2023-05-25 03:44:41',4),(59,29,'page_1','{}','{}','2023-05-26 00:00:42','2023-05-26 00:00:42',3),(60,30,'page_1','{}','{}','2023-05-26 00:03:27','2023-05-26 00:03:27',3),(61,31,'page_1','{}','{}','2023-05-26 04:20:05','2023-05-26 04:20:05',3),(62,31,'page_1','{}','{}','2023-05-26 04:22:05','2023-05-26 04:22:05',3),(63,32,'page_1','{}','{}','2023-05-30 07:38:12','2023-05-30 07:38:12',3),(64,33,'page_2','{}','{}','2023-05-30 07:45:28','2023-05-30 07:45:28',3),(65,33,'page_1','{}','{}','2023-05-30 07:45:45','2023-05-30 07:45:45',3),(66,34,'page_2','{}','{}','2023-05-30 07:56:26','2023-05-30 07:56:26',3),(67,34,'page_1','{}','{}','2023-05-30 07:56:42','2023-05-30 07:56:42',3),(68,35,'page_1','{}','{}','2023-05-30 08:11:00','2023-05-30 08:11:00',3),(69,36,'page_1','{}','{}','2023-05-30 08:11:23','2023-05-30 08:11:23',3),(70,37,'page_1','{}','{}','2023-06-06 08:21:14','2023-06-06 08:21:14',3),(71,39,'page_2','{}','{}','2023-06-08 00:42:34','2023-06-08 00:42:34',3),(72,39,'page_1','{}','{}','2023-06-08 00:42:48','2023-06-08 00:42:48',3),(73,40,'DISH FOOD','{}','{}','2023-06-08 23:58:08','2023-06-08 23:58:08',3),(74,41,'PO_3','{}','{}','2023-06-09 02:10:32','2023-06-09 02:10:32',3);
/*!40000 ALTER TABLE `tbl_extracted_doc` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-12  2:41:17
