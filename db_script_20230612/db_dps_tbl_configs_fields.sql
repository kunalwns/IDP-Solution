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
-- Table structure for table `tbl_configs_fields`
--

DROP TABLE IF EXISTS `tbl_configs_fields`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tbl_configs_fields` (
  `id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `config_id` int DEFAULT NULL,
  `field_name` varchar(45) DEFAULT NULL,
  `key_name` varchar(100) DEFAULT NULL,
  `field_datatype` varchar(45) DEFAULT NULL,
  `field_type` varchar(45) DEFAULT NULL,
  `sub_type` varchar(45) DEFAULT NULL,
  `questions` varchar(5000) DEFAULT NULL,
  `is_active` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=88 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tbl_configs_fields`
--

LOCK TABLES `tbl_configs_fields` WRITE;
/*!40000 ALTER TABLE `tbl_configs_fields` DISABLE KEYS */;
INSERT INTO `tbl_configs_fields` VALUES (1,3,1,'patient_name','patient_name','String','Form','custom','What is patient name',1),(2,3,1,'patient_address','patient_address','String','Form','custom','What is patient address',1),(3,3,1,'primary_insurance',NULL,'String','Form','custom','What is primary insurance for patient',1),(4,3,1,'physician_name','physician_name','String','Form','custom','What is physician name',1),(5,3,1,'physician_speciality',NULL,'String','Form','custom','What is physician speciality',1),(6,3,1,'medication',NULL,'String','Form','custom','What is medication',1),(7,3,1,'naproxen_therapy',NULL,'String','Form','custom','What is Naproxen Therapy date',1),(8,3,2,'patient_name',NULL,'String','Form','custom','What is the patient name',1),(9,3,2,'patient_last_name',NULL,'String','Form','custom','What is the patient last',1),(10,3,3,'Patient Name','patient_name','String','Form','custom','What is patient name',1),(12,3,3,'gender','gender','String','Form','custom','What is patient gender',1),(13,3,3,'street_line_1','street_line_1','String','Form','custom','What is patient address',1),(14,3,3,'patient_city','patient_city','String','Form','custom','What is patient city name',1),(15,3,3,'patient_state','patient_state','String','Form','custom','What is patient state name',1),(16,3,3,'patient_zip','patient_zip','String','Form','custom','What is patient address zip code',1),(17,3,3,'form_type','form_type','String','Form','custom','What type of this form is',1),(18,3,3,'claim_no','claim_no','String','Form','custom','What is claim number',1),(19,3,3,'DOL','DOL','String','Form','Custom','What is DOL',1),(20,3,3,'DOS','DOS','String','Form','Custom','What is DOS',1),(21,3,3,'Is Auto accident','is_auto_accident','String','Form','Custom','Is Auto Accident',1),(22,3,3,'Provider Name','provider_name','String','Form','Custom','What is service provider name',1),(23,3,3,'Group Name','group_name','String','Form','Custom','What is service provider group Name',1),(24,3,3,'TIN','tin','String','Form','Custom','What is service provider TIN',1),(25,3,3,'Service Provider Address','service_provider_address','String','Form','Custom','What is service provider street address',1),(26,3,3,'service provider city name','service_provider_city_name','String','Form','Custom','What is service provider city name',1),(27,3,3,'service provider state name','service_provider_state_name','String','Form','Custom','What is service provider state name',1),(28,3,3,'service provider zip code','service_provider_zip_code','String','Form','Custom','What is service provider zip code',1),(29,3,3,'provider name','billing_provider_name','String','Form','Custom','What is billing provider name',1),(30,3,3,'provider group name','billing_provider_group_name','String','Form','Custom','What is billing group name',1),(32,3,3,'billing provider TIN','billing_provider_TIN','String','Form','Custom','What is billing provider TIN',1),(33,3,3,'provider License type','billing_provider_license_type','String','Form','Custom','What is billing License type',1),(34,3,3,'provider Speciality','billing_provider_speciality','String','Form','Custom','What is billing provider Speciality',1),(35,3,3,'provider Bill Type','billing_provider_bill_type','String','Form','Custom','What is billing provider Bill Type',1),(36,3,3,'Provider Address','provider_address','String','Form','Custom','Provider street address',1),(37,3,3,'Provider city','provider_city','String','Form','Custom','Provider city name',1),(38,3,3,'Provider state name','provider_state_name','String','Form','Custom','Provider state name',1),(39,3,3,'Provider zip code','provider_zip_code','String','Form','Custom','Provider zip code',1),(40,3,3,'Billing Zip Code','billing_zip_code','String','Form','Custom','what is Process Billing Process Zip Code',1),(41,3,3,'Pickup Zip Code','billing_pickup_zip_code','String','Form','Custom','what is Process Billing Process Pickup Zip Code',1),(42,3,3,'Post Mark Date','billing_post_mark_date','String','Form','Custom','what is Process Billing  Post Mark Date',1),(43,3,3,'Type of bill','billing_type_of_bill','String','Form','Custom','what is Process Billing Type of bill',1),(44,3,3,'Box 14 on UB','box_14_on_UB','String','Form','Custom','what is Box 14 on UB',1),(45,3,3,'Bill Date','bill_date','String','Form','Custom','what is Bill Date',1),(46,3,3,'Tin Suffix','tin_suffix','String','Form','Custom','what is Tin Suffix',1),(47,3,3,'NPI no','npi_no','String','Form','Custom','what is NPI no',1),(54,3,18,'employer_name','emp_name','String','Form','custom','what is employer name',1),(55,3,18,'mobile','emp_mobile','String','Form','custom','Employer telephone number',1),(56,3,18,'total_amount','total_amount','String','Form','custom','what is total amount paid',1),(57,3,19,'patient_name','','String','Form','custom','what is patient name',1),(58,3,3,'DOB','patient_dob','String','Form','Custom','What is Patient Date of birth',1),(59,3,20,'patient_name','','String','Form','custom','What is patient name',1),(60,3,20,'doctor_name','','String','Form','custom','What is Doctor name',1),(61,3,20,'Dob','','String','Form','Custom','What is dob',1),(62,3,21,'doctor_name','','String','Form','custom','What is doctor name',1),(63,3,21,'patient_name','','String','Form','custom','What is patient name',1),(64,3,22,'company_name','','String','Form','custom','what is company name',1),(65,3,22,'Sender Account','','String','Form','Custom','sender account no',1),(66,3,22,'Receiver Account','','String','Form','Custom','receiver account no',1),(67,3,22,'receiver name','','String','Form','Custom','what is receiver name',1),(68,3,22,'sender zip code','','String','Form','Custom','sender zip code',1),(69,3,22,'sender location','','String','Form','Custom','Sender location',1),(70,3,22,'sender tel no','','String','Form','Custom','Sender tel no',1),(71,3,22,'Receiver Location','','String','Form','Custom','Receiver Location',1),(72,3,22,'Receiver address','','String','Form','Custom','Receiver address',1),(73,3,22,'Receiver zip code','','String','Form','Custom','Receiver zip code',1),(74,3,22,'Contact Name','','String','Form','Custom','Receiver contact Name',1),(75,3,22,'Delivery Address','','String','Form','Custom','what is delivery address',1),(76,3,22,'City Name','','String','Form','Custom','What is city name',1),(77,3,23,'patient_name','','String','Form','custom','what is the patient name',1),(78,3,23,'doctor_name','','String','Form','custom','what is the doctor name',1),(79,3,24,'patient_name','','String','Form','custom','what is the patient name',1),(80,3,25,'patient_name','','String','Form','custom','What is the patient name',1),(81,3,25,'doctor_name','','String','Form','custom','What is the doctor name',1),(82,3,26,'patient_name','','String','Form','custom','What is the patient name',1),(83,3,22,'Receiver postalcode','','String','Form','Custom','What is the receiver address zipcode or postcode',1),(84,3,27,'invoice_number','','String','Form','custom','what is invoice number',1),(85,3,27,'invoice_date','','String','Form','custom','what is invoice date',1),(86,3,27,'sub_total','','String','Form','custom','what is sub total',1),(87,3,27,'tax','','String','Form','custom','what is tax amount',1);
/*!40000 ALTER TABLE `tbl_configs_fields` ENABLE KEYS */;
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
