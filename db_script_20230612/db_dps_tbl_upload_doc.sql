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
-- Table structure for table `tbl_upload_doc`
--

DROP TABLE IF EXISTS `tbl_upload_doc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_upload_doc` (
  `id` int NOT NULL AUTO_INCREMENT,
  `doc_uuid` varchar(50) DEFAULT NULL,
  `company_id` int DEFAULT NULL,
  `doc_name` varchar(45) DEFAULT NULL,
  `doc_type` varchar(45) DEFAULT NULL,
  `config_id` varchar(45) DEFAULT NULL,
  `uploaded_by` int DEFAULT NULL,
  `uploaded_date` datetime DEFAULT NULL,
  `status` int DEFAULT NULL,
  `process_type` varchar(45) DEFAULT 'doc',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_upload_doc`
--

LOCK TABLES `tbl_upload_doc` WRITE;
/*!40000 ALTER TABLE `tbl_upload_doc` DISABLE KEYS */;
INSERT INTO `tbl_upload_doc` VALUES (12,'d4f52c18-f07f-11ed-aa9c-8d4f9ad018d7',3,'Sample Form.pdf','pdf','1',1,'2023-05-12 04:45:34',3,NULL),(13,'958a627e-f0ba-11ed-aa9c-8d4f9ad018d7',3,'Sample Form.pdf','pdf','3',1,'2023-05-12 11:46:08',3,NULL),(14,'c43d71fe-f2e2-11ed-aa9c-8d4f9ad018d7',3,'Sample Form.pdf','pdf','1',1,'2023-05-15 05:38:48',3,'doc'),(15,'a3a7c9f4-f3d1-11ed-b5bb-63e9c34ee15e',3,'claim_15.jpg','jpg','1',1,'2023-05-16 10:08:43',3,'doc'),(16,'cd66a472-f47b-11ed-b5bb-63e9c34ee15e',3,'claim_15.jpg','jpg','1',1,'2023-05-17 06:26:48',3,'doc'),(17,'2dd4c4c8-f47d-11ed-b5bb-63e9c34ee15e',3,'Sample Form.pdf','pdf','1',1,'2023-05-17 06:36:39',3,'doc'),(18,'8ac15be2-f487-11ed-b5bb-63e9c34ee15e',3,'756-csd.pdf','pdf','21',1,'2023-05-17 07:50:50',3,'doc'),(19,'b73f44d6-f572-11ed-83d2-2dfa9ccde725',3,'page_1.jpg','jpg','1',1,'2023-05-18 11:54:16',3,'doc'),(20,'d3752592-f93e-11ed-a60f-15faed2414d8',3,'133658668.pdf','pdf','22',1,'2023-05-23 07:52:54',3,'doc'),(21,'01d5248c-f953-11ed-a60f-15faed2414d8',3,'443788643.pdf','pdf','22',1,'2023-05-23 10:17:22',3,'doc'),(22,'29a82680-f953-11ed-a60f-15faed2414d8',3,'746249266.pdf','pdf','22',1,'2023-05-23 10:18:29',3,'doc'),(23,'799b2208-f955-11ed-a60f-15faed2414d8',3,'520912481.pdf','pdf','22',1,'2023-05-23 10:35:02',3,'doc'),(24,'4cce1aa0-f9e6-11ed-a60f-15faed2414d8',3,'521191485.pdf','pdf','22',1,'2023-05-24 03:51:44',4,'doc'),(25,'5d867ca6-f9f1-11ed-a60f-15faed2414d8',3,'746249266.pdf','pdf','22',1,'2023-05-24 05:10:56',3,'doc'),(26,'27ce8bde-f9f2-11ed-a60f-15faed2414d8',3,'claim_8.jpg','jpg','21',1,'2023-05-24 05:16:36',3,'doc'),(27,'ab1b8d36-fa09-11ed-a60f-15faed2414d8',3,'Sample Form.pdf','pdf','1',1,'2023-05-24 08:04:55',3,'doc'),(28,'bc712928-fa0f-11ed-a60f-15faed2414d8',3,'Sample Form.pdf','pdf','1',1,'2023-05-24 08:48:21',3,'doc'),(29,'c480ff80-fabe-11ed-a60f-15faed2414d8',3,'Sample Form.pdf','pdf','1',1,'2023-05-25 05:41:16',3,'doc'),(30,'fa3c5b36-facf-11ed-a60f-15faed2414d8',3,'Sample Form.pdf','pdf','1',1,'2023-05-25 07:44:28',3,'doc'),(31,'18d763c8-fb9e-11ed-a10f-a1c8e86a82f0',3,'Sample Form.pdf','pdf','1',1,'2023-05-26 08:19:55',3,'doc'),(32,'60e23b96-fede-11ed-886c-c5d939dd003f',3,'521242244.pdf','pdf','22',1,'2023-05-30 11:37:37',3,'doc'),(33,'6aca8d60-fedf-11ed-886c-c5d939dd003f',3,'303974636.pdf','pdf','22',1,'2023-05-30 11:45:04',3,'doc'),(34,'f2965a16-fee0-11ed-886c-c5d939dd003f',3,'695361374.pdf','pdf','22',1,'2023-05-30 11:56:01',3,'doc'),(35,'fde34968-fee2-11ed-886c-c5d939dd003f',3,'746249266.pdf','pdf','22',1,'2023-05-30 12:10:39',3,'doc'),(36,'0b2376de-fee3-11ed-886c-c5d939dd003f',3,'443788643.pdf','pdf','22',1,'2023-05-30 12:11:01',3,'doc'),(37,'47ea192c-0462-11ee-918f-910fd4c6cba1',3,'DISH FOOD.pdf','pdf','1',1,'2023-06-06 12:04:25',3,'doc'),(38,'39e7a07c-0464-11ee-918f-910fd4c6cba1',3,'DISH FOOD.pdf','pdf','20',1,'2023-06-06 12:18:20',4,'doc'),(39,'67e936f4-05b6-11ee-8b3d-9b3ee623e1f1',3,'378681375.pdf','pdf','1',1,'2023-06-08 04:39:08',3,'doc'),(40,'ecade8b4-0677-11ee-953c-5d942dd4d7f6',3,'DISH FOOD.pdf','pdf','1',1,'2023-06-09 03:44:23',3,'doc'),(41,'4aa4a44e-068c-11ee-953c-5d942dd4d7f6',3,'PO_3.pdf','pdf','1',1,'2023-06-09 06:10:11',3,'invoice');
/*!40000 ALTER TABLE `tbl_upload_doc` ENABLE KEYS */;
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
