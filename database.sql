-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: hethongquanly
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `company` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Phone` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exportbill`
--

DROP TABLE IF EXISTS `exportbill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exportbill` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Date` date DEFAULT NULL,
  `Manager` int DEFAULT NULL,
  `Customer` int DEFAULT NULL,
  `TotalIncome` float DEFAULT NULL,
  `Discriminator` varchar(255) NOT NULL,
  `CustomerID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKExportBill754948` (`CustomerID`),
  CONSTRAINT `FKExportBill754948` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exportbill`
--

LOCK TABLES `exportbill` WRITE;
/*!40000 ALTER TABLE `exportbill` DISABLE KEYS */;
/*!40000 ALTER TABLE `exportbill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exportbill_listproduct`
--

DROP TABLE IF EXISTS `exportbill_listproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exportbill_listproduct` (
  `ExportBillID` int NOT NULL,
  `ExportBillIndex` int NOT NULL,
  `ListProduct` int DEFAULT NULL,
  PRIMARY KEY (`ExportBillID`,`ExportBillIndex`),
  CONSTRAINT `FKExportBill356848` FOREIGN KEY (`ExportBillID`) REFERENCES `exportbill` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exportbill_listproduct`
--

LOCK TABLES `exportbill_listproduct` WRITE;
/*!40000 ALTER TABLE `exportbill_listproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `exportbill_listproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `importbill`
--

DROP TABLE IF EXISTS `importbill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `importbill` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Date` date DEFAULT NULL,
  `Manager` int DEFAULT NULL,
  `Provider` int DEFAULT NULL,
  `ProviderID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKImportBill987470` (`ProviderID`),
  CONSTRAINT `FKImportBill987470` FOREIGN KEY (`ProviderID`) REFERENCES `provider` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `importbill`
--

LOCK TABLES `importbill` WRITE;
/*!40000 ALTER TABLE `importbill` DISABLE KEYS */;
/*!40000 ALTER TABLE `importbill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `importbill_listmaterial`
--

DROP TABLE IF EXISTS `importbill_listmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `importbill_listmaterial` (
  `ImportBillID` int NOT NULL,
  `ImportBillIndex` int NOT NULL,
  `ListMaterial` int DEFAULT NULL,
  PRIMARY KEY (`ImportBillID`,`ImportBillIndex`),
  CONSTRAINT `FKImportBill953085` FOREIGN KEY (`ImportBillID`) REFERENCES `importbill` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `importbill_listmaterial`
--

LOCK TABLES `importbill_listmaterial` WRITE;
/*!40000 ALTER TABLE `importbill_listmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `importbill_listmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `importedmaterial`
--

DROP TABLE IF EXISTS `importedmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `importedmaterial` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Material` int DEFAULT NULL,
  `Price` float NOT NULL,
  `ImportBillID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKImportedMa22595` (`ImportBillID`),
  CONSTRAINT `FKImportedMa22595` FOREIGN KEY (`ImportBillID`) REFERENCES `importbill` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `importedmaterial`
--

LOCK TABLES `importedmaterial` WRITE;
/*!40000 ALTER TABLE `importedmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `importedmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `material`
--

DROP TABLE IF EXISTS `material`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `material` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Type` varchar(255) DEFAULT NULL,
  `Desc` varchar(255) DEFAULT NULL,
  `Quantity` float DEFAULT NULL,
  `Discriminator` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `material`
--

LOCK TABLES `material` WRITE;
/*!40000 ALTER TABLE `material` DISABLE KEYS */;
/*!40000 ALTER TABLE `material` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialinproduct`
--

DROP TABLE IF EXISTS `materialinproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialinproduct` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `MaterialID` int NOT NULL,
  `ProductID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKMaterialIn394094` (`MaterialID`),
  KEY `FKMaterialIn278580` (`ProductID`),
  CONSTRAINT `FKMaterialIn278580` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ID`),
  CONSTRAINT `FKMaterialIn394094` FOREIGN KEY (`MaterialID`) REFERENCES `material` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialinproduct`
--

LOCK TABLES `materialinproduct` WRITE;
/*!40000 ALTER TABLE `materialinproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `materialinproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialofprovider`
--

DROP TABLE IF EXISTS `materialofprovider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialofprovider` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Material` int DEFAULT NULL,
  `Price` float NOT NULL,
  `Provider` int DEFAULT NULL,
  `ImportedMaterialID` int NOT NULL,
  `ProviderID` int NOT NULL,
  `MaterialID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKMaterialOf753886` (`ImportedMaterialID`),
  KEY `FKMaterialOf56304` (`ProviderID`),
  KEY `FKMaterialOf725357` (`MaterialID`),
  CONSTRAINT `FKMaterialOf56304` FOREIGN KEY (`ProviderID`) REFERENCES `provider` (`ID`),
  CONSTRAINT `FKMaterialOf725357` FOREIGN KEY (`MaterialID`) REFERENCES `material` (`ID`),
  CONSTRAINT `FKMaterialOf753886` FOREIGN KEY (`ImportedMaterialID`) REFERENCES `importedmaterial` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialofprovider`
--

LOCK TABLES `materialofprovider` WRITE;
/*!40000 ALTER TABLE `materialofprovider` DISABLE KEYS */;
/*!40000 ALTER TABLE `materialofprovider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialofproviderinstorage`
--

DROP TABLE IF EXISTS `materialofproviderinstorage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialofproviderinstorage` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `RequestedMaterialID` int DEFAULT NULL,
  `Material` int DEFAULT NULL,
  `Quantity` float NOT NULL,
  `StorageID` int NOT NULL,
  `MaterialOfProviderID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKMaterialOf448044` (`RequestedMaterialID`),
  KEY `FKMaterialOf397408` (`StorageID`),
  KEY `FKMaterialOf94305` (`MaterialOfProviderID`),
  CONSTRAINT `FKMaterialOf397408` FOREIGN KEY (`StorageID`) REFERENCES `storage` (`ID`),
  CONSTRAINT `FKMaterialOf448044` FOREIGN KEY (`RequestedMaterialID`) REFERENCES `requestedmaterial` (`ID`),
  CONSTRAINT `FKMaterialOf94305` FOREIGN KEY (`MaterialOfProviderID`) REFERENCES `materialofprovider` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialofproviderinstorage`
--

LOCK TABLES `materialofproviderinstorage` WRITE;
/*!40000 ALTER TABLE `materialofproviderinstorage` DISABLE KEYS */;
/*!40000 ALTER TABLE `materialofproviderinstorage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialrequest`
--

DROP TABLE IF EXISTS `materialrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialrequest` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `TaskID` int NOT NULL,
  `StorageID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKMaterialRe637200` (`TaskID`),
  KEY `FKMaterialRe710589` (`StorageID`),
  CONSTRAINT `FKMaterialRe637200` FOREIGN KEY (`TaskID`) REFERENCES `task` (`ID`),
  CONSTRAINT `FKMaterialRe710589` FOREIGN KEY (`StorageID`) REFERENCES `storage` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialrequest`
--

LOCK TABLES `materialrequest` WRITE;
/*!40000 ALTER TABLE `materialrequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `materialrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `materialrequest_listmaterial`
--

DROP TABLE IF EXISTS `materialrequest_listmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `materialrequest_listmaterial` (
  `MaterialRequestID` int NOT NULL,
  `MaterialRequestIndex` int NOT NULL,
  `ListMaterial` int DEFAULT NULL,
  PRIMARY KEY (`MaterialRequestID`,`MaterialRequestIndex`),
  CONSTRAINT `FKMaterialRe684193` FOREIGN KEY (`MaterialRequestID`) REFERENCES `materialrequest` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `materialrequest_listmaterial`
--

LOCK TABLES `materialrequest_listmaterial` WRITE;
/*!40000 ALTER TABLE `materialrequest_listmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `materialrequest_listmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Customer` int DEFAULT NULL,
  `CustomerID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKOrder556711` (`CustomerID`),
  CONSTRAINT `FKOrder556711` FOREIGN KEY (`CustomerID`) REFERENCES `customer` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_listproduct`
--

DROP TABLE IF EXISTS `order_listproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_listproduct` (
  `OrderID` int NOT NULL,
  `OrderIndex` int NOT NULL,
  `ListProduct` int DEFAULT NULL,
  PRIMARY KEY (`OrderID`,`OrderIndex`),
  CONSTRAINT `FKOrder_list193811` FOREIGN KEY (`OrderID`) REFERENCES `order` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_listproduct`
--

LOCK TABLES `order_listproduct` WRITE;
/*!40000 ALTER TABLE `order_listproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `order_listproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderedproduct`
--

DROP TABLE IF EXISTS `orderedproduct`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderedproduct` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `StorageID` int NOT NULL,
  `Price` float NOT NULL,
  `Product` int DEFAULT NULL,
  `Quantity` int NOT NULL,
  `ProductExportedID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKOrderedPro960490` (`StorageID`),
  KEY `FKOrderedPro835304` (`ProductExportedID`),
  CONSTRAINT `FKOrderedPro835304` FOREIGN KEY (`ProductExportedID`) REFERENCES `productexported` (`ID`),
  CONSTRAINT `FKOrderedPro960490` FOREIGN KEY (`StorageID`) REFERENCES `storage` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderedproduct`
--

LOCK TABLES `orderedproduct` WRITE;
/*!40000 ALTER TABLE `orderedproduct` DISABLE KEYS */;
/*!40000 ALTER TABLE `orderedproduct` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Type` varchar(255) DEFAULT NULL,
  `Price` float NOT NULL,
  `Desc` varchar(255) DEFAULT NULL,
  `IdDesign` varchar(255) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Discriminator` varchar(255) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_listmaterial`
--

DROP TABLE IF EXISTS `product_listmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_listmaterial` (
  `ProductID` int NOT NULL,
  `ProductIndex` int NOT NULL,
  `ListMaterial` int DEFAULT NULL,
  PRIMARY KEY (`ProductID`,`ProductIndex`),
  CONSTRAINT `FKProduct_li693288` FOREIGN KEY (`ProductID`) REFERENCES `product` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_listmaterial`
--

LOCK TABLES `product_listmaterial` WRITE;
/*!40000 ALTER TABLE `product_listmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `product_listmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productexported`
--

DROP TABLE IF EXISTS `productexported`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productexported` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Quantity` int NOT NULL,
  `Price` float NOT NULL,
  `Product` int DEFAULT NULL,
  `ExportBillID` int NOT NULL,
  `ProductID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKProductExp892789` (`ExportBillID`),
  CONSTRAINT `FKProductExp892789` FOREIGN KEY (`ExportBillID`) REFERENCES `exportbill` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productexported`
--

LOCK TABLES `productexported` WRITE;
/*!40000 ALTER TABLE `productexported` DISABLE KEYS */;
/*!40000 ALTER TABLE `productexported` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `progress`
--

DROP TABLE IF EXISTS `progress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `progress` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `progress`
--

LOCK TABLES `progress` WRITE;
/*!40000 ALTER TABLE `progress` DISABLE KEYS */;
/*!40000 ALTER TABLE `progress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider`
--

DROP TABLE IF EXISTS `provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `provider` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone` varchar(255) DEFAULT NULL,
  `Desc` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider`
--

LOCK TABLES `provider` WRITE;
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requestedmaterial`
--

DROP TABLE IF EXISTS `requestedmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requestedmaterial` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Material` int DEFAULT NULL,
  `Quantity` float NOT NULL,
  `MaterialRequestID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKRequestedM697480` (`MaterialRequestID`),
  CONSTRAINT `FKRequestedM697480` FOREIGN KEY (`MaterialRequestID`) REFERENCES `materialrequest` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requestedmaterial`
--

LOCK TABLES `requestedmaterial` WRITE;
/*!40000 ALTER TABLE `requestedmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `requestedmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Desc` varchar(255) DEFAULT NULL,
  `Manager` int DEFAULT NULL,
  `CompanyID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKStorage300049` (`CompanyID`),
  CONSTRAINT `FKStorage300049` FOREIGN KEY (`CompanyID`) REFERENCES `company` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storage_listmaterial`
--

DROP TABLE IF EXISTS `storage_listmaterial`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage_listmaterial` (
  `StorageID` int NOT NULL,
  `StorageIndex` int NOT NULL,
  `ListMaterial` int DEFAULT NULL,
  PRIMARY KEY (`StorageID`,`StorageIndex`),
  CONSTRAINT `FKStorage_li925075` FOREIGN KEY (`StorageID`) REFERENCES `storage` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage_listmaterial`
--

LOCK TABLES `storage_listmaterial` WRITE;
/*!40000 ALTER TABLE `storage_listmaterial` DISABLE KEYS */;
/*!40000 ALTER TABLE `storage_listmaterial` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `OrderedProductID` int NOT NULL,
  `Product` int DEFAULT NULL,
  `UserID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKTask321858` (`OrderedProductID`),
  KEY `FKTask917857` (`UserID`),
  CONSTRAINT `FKTask321858` FOREIGN KEY (`OrderedProductID`) REFERENCES `orderedproduct` (`ID`),
  CONSTRAINT `FKTask917857` FOREIGN KEY (`UserID`) REFERENCES `user` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_listprogress`
--

DROP TABLE IF EXISTS `task_listprogress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_listprogress` (
  `TaskID` int NOT NULL,
  `TaskIndex` int NOT NULL,
  `ListProgress` int DEFAULT NULL,
  PRIMARY KEY (`TaskID`,`TaskIndex`),
  CONSTRAINT `FKTask_listP899648` FOREIGN KEY (`TaskID`) REFERENCES `task` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_listprogress`
--

LOCK TABLES `task_listprogress` WRITE;
/*!40000 ALTER TABLE `task_listprogress` DISABLE KEYS */;
/*!40000 ALTER TABLE `task_listprogress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_listrequest`
--

DROP TABLE IF EXISTS `task_listrequest`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_listrequest` (
  `TaskID` int NOT NULL,
  `TaskIndex` int NOT NULL,
  `ListRequest` int DEFAULT NULL,
  PRIMARY KEY (`TaskID`,`TaskIndex`),
  CONSTRAINT `FKTask_listR309720` FOREIGN KEY (`TaskID`) REFERENCES `task` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_listrequest`
--

LOCK TABLES `task_listrequest` WRITE;
/*!40000 ALTER TABLE `task_listrequest` DISABLE KEYS */;
/*!40000 ALTER TABLE `task_listrequest` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `taskprogress`
--

DROP TABLE IF EXISTS `taskprogress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `taskprogress` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Progress` int DEFAULT NULL,
  `Task` int DEFAULT NULL,
  `StartDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  `TaskID` int NOT NULL,
  `ProgressID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKTaskProgre236977` (`TaskID`),
  KEY `FKTaskProgre793853` (`ProgressID`),
  CONSTRAINT `FKTaskProgre236977` FOREIGN KEY (`TaskID`) REFERENCES `task` (`ID`),
  CONSTRAINT `FKTaskProgre793853` FOREIGN KEY (`ProgressID`) REFERENCES `progress` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `taskprogress`
--

LOCK TABLES `taskprogress` WRITE;
/*!40000 ALTER TABLE `taskprogress` DISABLE KEYS */;
/*!40000 ALTER TABLE `taskprogress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Phone` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Username` varchar(255) DEFAULT NULL,
  `Password` varchar(255) DEFAULT NULL,
  `Discriminator` varchar(255) NOT NULL,
  `CompanyID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKUser33059` (`CompanyID`),
  CONSTRAINT `FKUser33059` FOREIGN KEY (`CompanyID`) REFERENCES `company` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workshop`
--

DROP TABLE IF EXISTS `workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `workshop` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `Desc` varchar(255) DEFAULT NULL,
  `CompanyID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FKWorkshop272261` (`CompanyID`),
  CONSTRAINT `FKWorkshop272261` FOREIGN KEY (`CompanyID`) REFERENCES `company` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workshop`
--

LOCK TABLES `workshop` WRITE;
/*!40000 ALTER TABLE `workshop` DISABLE KEYS */;
/*!40000 ALTER TABLE `workshop` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-03 11:20:27
