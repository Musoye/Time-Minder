-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: time_master
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.22.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `user_id` varchar(60) NOT NULL,
  `name` varchar(128) NOT NULL,
  `description` varchar(128) DEFAULT NULL,
  `sent` tinyint(1) DEFAULT NULL,
  `expiry_date` datetime DEFAULT NULL,
  `is_priority` tinyint(1) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES ('d97fadf2-7879-433e-b1af-4ff1f672ef36','The Markonikov Theory','The Theory of Markonikov in organic chemistry',0,'2023-05-29 15:55:04',0,'1f912038-cc79-4171-9b47-5891dd41d2d1','2023-05-26 15:55:20','2023-05-26 15:55:20'),('d97fadf2-7879-433e-b1af-4ff1f672ef36','The Markonikov Theory','The Theory of Markonikov in organic chemistry',0,'2023-05-27 06:57:24',0,'4288cfb3-1f4c-498c-b223-250cbf171ee2','2023-05-24 06:58:08','2023-05-24 06:58:08'),('d97fadf2-7879-433e-b1af-4ff1f672ef36','The Markonikov Theory','The Theory of Markonikov in organic chemistry',0,'2023-05-27 06:57:24',0,'4b7cfe63-cad3-4448-b0bf-335ce942f474','2023-05-24 06:58:06','2023-05-24 06:58:06'),('d97fadf2-7879-433e-b1af-4ff1f672ef36','The Markonikov Theory','The Theory of Markonikov in organic chemistry',0,'2023-05-27 06:35:58',0,'63d67f6c-5780-477c-ba01-d4e6171fb781','2023-05-24 06:38:11','2023-05-24 06:38:11'),('eac5e5bf-0005-4da1-9b2a-bea787dc29eb','Mustapha The master','Mustapha the Master is the story of a young African boy who is going on the path of being the greatest',0,'2023-06-10 22:39:30',0,'7101372d-4bf1-4b8b-8727-d7e23cac5ba7','2023-06-07 23:16:18','2023-06-07 23:16:18'),('d7d05a45-edf8-4c2e-90f1-502c205bca77','The design','The Product design',0,'2023-05-27 06:35:58',0,'9957604f-b048-4319-a6c7-c9e00623a393','2023-05-24 06:36:05','2023-05-24 06:36:05'),('d7d05a45-edf8-4c2e-90f1-502c205bca77','the odion project',NULL,0,'2023-05-26 14:55:39',0,'abd23c36-ba06-44fe-bd38-44d921c6cdb6','2023-05-23 13:57:32','2023-05-23 15:01:23'),('d97fadf2-7879-433e-b1af-4ff1f672ef36','The Markonikov Theory','The Theory of Markonikov in organic chemistry',0,'2023-05-27 06:57:24',0,'ba89be7d-4643-4bd0-9005-8fd743bbece1','2023-05-24 06:58:06','2023-05-24 06:58:06');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tasks`
--

DROP TABLE IF EXISTS `tasks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tasks` (
  `project_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `name` varchar(128) NOT NULL,
  `status` varchar(16) NOT NULL,
  `description` varchar(128) DEFAULT NULL,
  `sent` tinyint(1) DEFAULT NULL,
  `expiry_date` datetime DEFAULT NULL,
  `is_priority` tinyint(1) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `project_id` (`project_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `tasks_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`),
  CONSTRAINT `tasks_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tasks`
--

LOCK TABLES `tasks` WRITE;
/*!40000 ALTER TABLE `tasks` DISABLE KEYS */;
INSERT INTO `tasks` VALUES ('abd23c36-ba06-44fe-bd38-44d921c6cdb6','d7d05a45-edf8-4c2e-90f1-502c205bca77','The interface','doing',NULL,0,'2023-05-26 15:03:18',0,'21cc7e32-a02d-49ec-83c7-0d4899490f8e','2023-05-23 14:03:33','2023-05-23 15:05:01'),('63d67f6c-5780-477c-ba01-d4e6171fb781','d97fadf2-7879-433e-b1af-4ff1f672ef36','Introduction to Markonikov Theory','doing','Introduction into The Theory of Markonikov in organic chemistry',0,'2023-05-27 06:43:39',0,'5e91a431-239b-4d5b-bf2a-b0ac0dc7cfd2','2023-05-24 06:43:45','2023-05-24 06:43:45');
/*!40000 ALTER TABLE `tasks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `email` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `first_name` varchar(128) DEFAULT NULL,
  `last_name` varchar(128) DEFAULT NULL,
  `is_suscribe` tinyint(1) DEFAULT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('mus@mus.com','af3e333de47c9f19e2024a5f5c314812',NULL,NULL,1,'d7d05a45-edf8-4c2e-90f1-502c205bca77','2023-05-23 13:55:51','2023-05-26 15:28:11'),('mymail@mail.com','3316862d315faa3c1e8dde2d379ee8c9','firste','last',1,'d97fadf2-7879-433e-b1af-4ff1f672ef36','2023-05-24 06:28:48','2023-06-07 22:52:55'),('mmusoye@gmail.com','96721002e79e783ecf22eac6543c3bfb',NULL,'Oyebamiji',1,'eac5e5bf-0005-4da1-9b2a-bea787dc29eb','2023-06-07 22:59:37','2023-06-07 22:59:37');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-10 14:10:13
