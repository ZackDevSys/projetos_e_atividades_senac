-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: torquehub_db
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.32-MariaDB

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
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `cpf` varchar(14) DEFAULT NULL,
  `telefone` varchar(20) NOT NULL,
  `email` varchar(150) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `observacoes` text DEFAULT NULL,
  `status` enum('ATIVO','INATIVO') NOT NULL DEFAULT 'ATIVO',
  `data_cadastro` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `telefone` (`telefone`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `email` (`email`),
  KEY `idx_clientes_nome` (`nome`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'João da Silva Atualizado','12323868901','31988888888','joao.atualizado@torquehub.com','Avenida TorqueHub, 500','Cliente de teste','ATIVO','2026-08-12 13:40:45'),(2,'Marcos Oliveira','987.654.321-00','(31) 97777-0002','marcos@email.com','Belo Horizonte - MG','Cliente de teste','ATIVO','2026-08-12 13:40:45');
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itens_pecas`
--

DROP TABLE IF EXISTS `itens_pecas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itens_pecas` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ordem_servico_id` int(10) unsigned NOT NULL,
  `peca_id` int(10) unsigned NOT NULL,
  `quantidade` int(10) unsigned NOT NULL DEFAULT 1,
  `valor_unitario` decimal(10,2) NOT NULL DEFAULT 0.00,
  `valor_total` decimal(10,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`id`),
  KEY `fk_item_peca_peca` (`peca_id`),
  KEY `idx_itens_pecas_os` (`ordem_servico_id`),
  CONSTRAINT `fk_item_peca_os` FOREIGN KEY (`ordem_servico_id`) REFERENCES `ordens_servico` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_item_peca_peca` FOREIGN KEY (`peca_id`) REFERENCES `pecas` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `chk_item_peca_quantidade` CHECK (`quantidade` > 0),
  CONSTRAINT `chk_item_peca_valor` CHECK (`valor_unitario` >= 0),
  CONSTRAINT `chk_item_peca_total` CHECK (`valor_total` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itens_pecas`
--

LOCK TABLES `itens_pecas` WRITE;
/*!40000 ALTER TABLE `itens_pecas` DISABLE KEYS */;
INSERT INTO `itens_pecas` VALUES (1,1,1,2,45.00,90.00),(2,1,2,1,28.00,28.00);
/*!40000 ALTER TABLE `itens_pecas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itens_servico`
--

DROP TABLE IF EXISTS `itens_servico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `itens_servico` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ordem_servico_id` int(10) unsigned NOT NULL,
  `servico_id` int(10) unsigned NOT NULL,
  `quantidade` decimal(10,2) NOT NULL DEFAULT 1.00,
  `valor_unitario` decimal(10,2) NOT NULL DEFAULT 0.00,
  `valor_total` decimal(10,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`id`),
  KEY `fk_item_servico_servico` (`servico_id`),
  KEY `idx_itens_servico_os` (`ordem_servico_id`),
  CONSTRAINT `fk_item_servico_os` FOREIGN KEY (`ordem_servico_id`) REFERENCES `ordens_servico` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_item_servico_servico` FOREIGN KEY (`servico_id`) REFERENCES `servicos` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `chk_item_servico_quantidade` CHECK (`quantidade` > 0),
  CONSTRAINT `chk_item_servico_valor` CHECK (`valor_unitario` >= 0),
  CONSTRAINT `chk_item_servico_total` CHECK (`valor_total` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itens_servico`
--

LOCK TABLES `itens_servico` WRITE;
/*!40000 ALTER TABLE `itens_servico` DISABLE KEYS */;
INSERT INTO `itens_servico` VALUES (1,1,5,1.00,100.00,100.00),(2,1,3,1.00,120.00,120.00),(3,1,1,1.00,80.00,80.00);
/*!40000 ALTER TABLE `itens_servico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movimentacoes_estoque`
--

DROP TABLE IF EXISTS `movimentacoes_estoque`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movimentacoes_estoque` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `peca_id` int(10) unsigned NOT NULL,
  `usuario_id` int(10) unsigned NOT NULL,
  `tipo` enum('ENTRADA','SAIDA') NOT NULL,
  `quantidade` int(10) unsigned NOT NULL,
  `data` datetime NOT NULL DEFAULT current_timestamp(),
  `observacao` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_movimentacoes_peca` (`peca_id`),
  KEY `idx_movimentacoes_usuario` (`usuario_id`),
  CONSTRAINT `fk_movimentacao_peca` FOREIGN KEY (`peca_id`) REFERENCES `pecas` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `fk_movimentacao_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `chk_movimentacao_quantidade` CHECK (`quantidade` > 0)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movimentacoes_estoque`
--

LOCK TABLES `movimentacoes_estoque` WRITE;
/*!40000 ALTER TABLE `movimentacoes_estoque` DISABLE KEYS */;
INSERT INTO `movimentacoes_estoque` VALUES (1,1,1,'ENTRADA',10,'2026-08-12 14:07:50','Reposição inicial de estoque');
/*!40000 ALTER TABLE `movimentacoes_estoque` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordem_servico_usuario`
--

DROP TABLE IF EXISTS `ordem_servico_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordem_servico_usuario` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `ordem_servico_id` int(10) unsigned NOT NULL,
  `usuario_id` int(10) unsigned NOT NULL,
  `perfil` varchar(30) NOT NULL,
  `data_atribuicao` datetime NOT NULL DEFAULT current_timestamp(),
  `observacoes` text DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_os_usuario_perfil` (`ordem_servico_id`,`usuario_id`,`perfil`),
  KEY `idx_os_usuario_ordem` (`ordem_servico_id`),
  KEY `idx_os_usuario_usuario` (`usuario_id`),
  KEY `idx_os_usuario_perfil` (`perfil`),
  CONSTRAINT `fk_os_usuario_ordem` FOREIGN KEY (`ordem_servico_id`) REFERENCES `ordens_servico` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_os_usuario_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordem_servico_usuario`
--

LOCK TABLES `ordem_servico_usuario` WRITE;
/*!40000 ALTER TABLE `ordem_servico_usuario` DISABLE KEYS */;
INSERT INTO `ordem_servico_usuario` VALUES (1,1,2,'MECANICO','2026-08-13 16:31:41','Responsável pela execução do serviço'),(4,5,2,'MECANICO','2026-08-13 16:53:41',NULL),(5,5,4,'ESTOQUISTA','2026-08-13 16:53:41',NULL),(6,3,2,'MECANICO','2026-08-13 16:56:52',NULL),(7,3,4,'ESTOQUISTA','2026-08-13 16:56:52',NULL),(8,3,7,'ESTOQUISTA','2026-08-13 16:56:52',NULL),(9,1,4,'ESTOQUISTA','2026-08-13 17:24:45','Responsável pela separação das peças.'),(12,1,3,'MECANICO','2026-08-13 17:25:53','Responsável pela manutenção mecânica.');
/*!40000 ALTER TABLE `ordem_servico_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordens_servico`
--

DROP TABLE IF EXISTS `ordens_servico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ordens_servico` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `numero` varchar(20) NOT NULL,
  `veiculo_id` int(10) unsigned NOT NULL,
  `data_entrada` datetime NOT NULL DEFAULT current_timestamp(),
  `previsao_entrega` datetime DEFAULT NULL,
  `data_conclusao` datetime DEFAULT NULL,
  `data_entrega` datetime DEFAULT NULL,
  `km_entrada` int(10) unsigned NOT NULL DEFAULT 0,
  `problema_relatado` text NOT NULL,
  `diagnostico` text DEFAULT NULL,
  `observacoes` text DEFAULT NULL,
  `status` enum('ABERTA','EM_ANALISE','AGUARDANDO_APROVACAO','EM_MANUTENCAO','AGUARDANDO_PECA','FINALIZADA','ENTREGUE','CANCELADA') NOT NULL DEFAULT 'ABERTA',
  `valor_total` decimal(10,2) NOT NULL DEFAULT 0.00,
  PRIMARY KEY (`id`),
  UNIQUE KEY `numero` (`numero`),
  KEY `idx_os_veiculo` (`veiculo_id`),
  KEY `idx_os_status` (`status`),
  KEY `idx_os_data_entrada` (`data_entrada`),
  CONSTRAINT `fk_os_veiculo` FOREIGN KEY (`veiculo_id`) REFERENCES `veiculos` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `chk_os_km` CHECK (`km_entrada` >= 0),
  CONSTRAINT `chk_os_valor` CHECK (`valor_total` >= 0),
  CONSTRAINT `chk_os_datas` CHECK (`previsao_entrega` is null or `previsao_entrega` >= `data_entrada`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordens_servico`
--

LOCK TABLES `ordens_servico` WRITE;
/*!40000 ALTER TABLE `ordens_servico` DISABLE KEYS */;
INSERT INTO `ordens_servico` VALUES (1,'OS-000001',1,'2026-08-12 13:56:44','2026-08-14 14:00:00',NULL,NULL,42500,'Motor apresentando falha durante aceleracao',NULL,'Cliente solicitou avaliacao.','ENTREGUE',300.00),(3,'OS-000002',1,'2026-08-13 14:00:00','2026-08-15 17:00:00',NULL,NULL,42500,'Motor apresentando falha na aceleração','Necessária avaliação e verificação de peças','Estoque deverá verificar disponibilidade das peças','AGUARDANDO_PECA',338.00),(5,'OS-000003',1,'2026-08-13 10:00:00','2026-08-14 17:00:00',NULL,NULL,42500,'Motor apresentando falha na aceleração','Em análise','Cliente solicitou avaliação completa','ABERTA',0.00);
/*!40000 ALTER TABLE `ordens_servico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pecas`
--

DROP TABLE IF EXISTS `pecas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pecas` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `codigo` varchar(50) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `fabricante` varchar(100) DEFAULT NULL,
  `descricao` text DEFAULT NULL,
  `preco_custo` decimal(10,2) NOT NULL DEFAULT 0.00,
  `preco_venda` decimal(10,2) NOT NULL DEFAULT 0.00,
  `estoque_atual` int(10) unsigned NOT NULL DEFAULT 0,
  `estoque_minimo` int(10) unsigned NOT NULL DEFAULT 0,
  `status` enum('ATIVO','INATIVO') NOT NULL DEFAULT 'ATIVO',
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  CONSTRAINT `chk_peca_preco_custo` CHECK (`preco_custo` >= 0),
  CONSTRAINT `chk_peca_preco_venda` CHECK (`preco_venda` >= 0),
  CONSTRAINT `chk_peca_estoque_minimo` CHECK (`estoque_minimo` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pecas`
--

LOCK TABLES `pecas` WRITE;
/*!40000 ALTER TABLE `pecas` DISABLE KEYS */;
INSERT INTO `pecas` VALUES (1,'OL10W40','Óleo 10W40','Motul','Óleo para motor',32.00,45.00,20,5,'ATIVO'),(2,'FIL-OLEO-001','Filtro de óleo','Original','Filtro de óleo para motocicletas',18.00,28.00,15,5,'ATIVO'),(3,'VELA-NGK-001','Vela de ignição','NGK','Vela de ignição',22.00,35.00,10,3,'ATIVO'),(4,'FIL-AR-001','Filtro de ar','Original','Filtro de ar',30.00,50.00,8,3,'ATIVO'),(5,'PAS-FREIO-001','Pastilha de freio','Cobreq','Pastilha de freio dianteira',55.00,90.00,6,2,'ATIVO');
/*!40000 ALTER TABLE `pecas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `servicos`
--

DROP TABLE IF EXISTS `servicos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `servicos` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `descricao` text DEFAULT NULL,
  `valor_base` decimal(10,2) NOT NULL DEFAULT 0.00,
  `tempo_estimado` int(10) unsigned DEFAULT NULL,
  `status` enum('ATIVO','INATIVO') NOT NULL DEFAULT 'ATIVO',
  PRIMARY KEY (`id`),
  CONSTRAINT `chk_servico_valor` CHECK (`valor_base` >= 0),
  CONSTRAINT `chk_servico_tempo` CHECK (`tempo_estimado` is null or `tempo_estimado` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `servicos`
--

LOCK TABLES `servicos` WRITE;
/*!40000 ALTER TABLE `servicos` DISABLE KEYS */;
INSERT INTO `servicos` VALUES (1,'Troca de óleo','Troca do óleo do motor e verificação básica',80.00,30,'ATIVO'),(2,'Revisão básica','Inspeção geral do veículo',150.00,90,'ATIVO'),(3,'Limpeza de bico injetor','Limpeza e verificação do sistema de injeção',120.00,60,'ATIVO'),(4,'Regulagem de válvulas','Regulagem das válvulas do motor',180.00,120,'ATIVO'),(5,'Diagnóstico eletrônico','Diagnóstico utilizando scanner',100.00,60,'ATIVO'),(6,'Manutenção de freios','Inspeção e manutenção do sistema de freios',150.00,90,'ATIVO'),(7,'Manutenção de suspensão','Inspeção e manutenção do sistema de suspensão',180.00,120,'ATIVO');
/*!40000 ALTER TABLE `servicos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `telefone` varchar(20) DEFAULT NULL,
  `perfil` varchar(30) NOT NULL DEFAULT 'FUNCIONARIO',
  `especialidade` varchar(100) DEFAULT NULL,
  `status` enum('ATIVO','INATIVO') NOT NULL DEFAULT 'ATIVO',
  `data_cadastro` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `telefone` (`telefone`),
  CONSTRAINT `chk_usuario_mecanico_especialidade` CHECK (`perfil` <> 'MECANICO' or `especialidade` is not null)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Administrador TorqueHub','admin@torquehub.local','Admin@123','(31) 99999-9999','ADMINISTRADOR',NULL,'ATIVO','2026-08-12 13:40:45'),(2,'Carlos Silva','carlos@torquehub.local','TEMPORARIO','(31) 98888-1111','MECANICO','Motor e Injeção Eletrônica','ATIVO','2026-08-12 13:40:45'),(3,'Rafael Souza','rafael@torquehub.local','TEMPORARIO','(31) 97777-2222','MECANICO','Freios e Suspensão','ATIVO','2026-08-12 13:40:45'),(4,'Carlos','carlos@torquehub.com','scrypt:32768:8:1$dJxYdS7s1H8THBLf$60089d86ee2cacb3384e24a8b406830909d1789b67e93ec1ac2f0c2c45942ae683fc01ece26c9305efad95eb9fd0394dadd218dbc3958ad5816e1e9bca75c5ae','31988888888','ESTOQUISTA',NULL,'ATIVO','2026-08-12 13:40:45'),(6,'João Mecânico','joao.mecanico@torquehub.com','scrypt:32768:8:1$w7CgTwEySlVOaP0a$23158b63ee2760b8f0126955b0a7c0ad15aadae820bea774704b45185d7a15fec938f70a868c42ae09bf579de0c98d6b686a9cbe97234c5e0a95f8a9f8935bdc','31999999999','MECANICO','Injeção eletrônica','ATIVO','2026-08-13 15:21:03'),(7,'Carlos Estoquista','carlos.estoque@torquehub.com','scrypt:32768:8:1$yt9KcQ1JihKW0B5m$136ae86723cf110b9f08d0cf0aa70595d0763fda2ce98c3556b55301502dcef252214d997e1ce79ed966428a2c5157a5b76e454635577d71889d7f14b45c3b6b','31888888888','ESTOQUISTA',NULL,'ATIVO','2026-08-13 15:21:25'),(8,'Maria Atendente','maria.atendimento@torquehub.com','scrypt:32768:8:1$snOrBa6ajw64mm6W$e72e743dc86f56b60d1efd36fc9c2863dc41a342a5e641c9df3a317ce9107f403763c1521b0c282c6a8ff98938ed14833955c32963844f14fb7f9eda61d9d8ae','31777777777','ATENDENTE',NULL,'ATIVO','2026-08-13 15:21:43');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veiculos`
--

DROP TABLE IF EXISTS `veiculos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veiculos` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `cliente_id` int(10) unsigned NOT NULL,
  `tipo` enum('MOTOCICLETA','CARRO','CAMINHONETE','VAN','UTILITARIO','OUTRO') NOT NULL DEFAULT 'MOTOCICLETA',
  `marca` varchar(50) NOT NULL,
  `modelo` varchar(80) NOT NULL,
  `ano` year(4) NOT NULL,
  `placa` varchar(10) DEFAULT NULL,
  `chassi` varchar(50) DEFAULT NULL,
  `cor` varchar(30) DEFAULT NULL,
  `quilometragem` int(10) unsigned NOT NULL DEFAULT 0,
  `observacoes` text DEFAULT NULL,
  `status` enum('ATIVO','INATIVO') NOT NULL DEFAULT 'ATIVO',
  `data_cadastro` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `placa` (`placa`),
  KEY `idx_veiculos_cliente` (`cliente_id`),
  KEY `idx_veiculos_placa` (`placa`),
  CONSTRAINT `fk_veiculo_cliente` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`) ON UPDATE CASCADE,
  CONSTRAINT `chk_veiculo_ano` CHECK (`ano` >= 1900),
  CONSTRAINT `chk_veiculo_quilometragem` CHECK (`quilometragem` >= 0)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veiculos`
--

LOCK TABLES `veiculos` WRITE;
/*!40000 ALTER TABLE `veiculos` DISABLE KEYS */;
INSERT INTO `veiculos` VALUES (1,1,'MOTOCICLETA','Honda','CG 160 Titan',2024,'ABC1D23','9C2KC0810XR123456','Vermelha',18500,'Revisão realizada.','ATIVO','2026-08-12 13:40:45'),(2,2,'MOTOCICLETA','Honda','CG 160 Titan',2022,'XYZ4E56',NULL,'Vermelha',18000,'Veículo de teste','ATIVO','2026-08-12 13:40:45'),(3,1,'CARRO','Volkswagen','Gol',2020,'DEF7G89',NULL,'Prata',35000,'Exemplo para testar expansão para carros','ATIVO','2026-08-12 13:40:45'),(6,1,'MOTOCICLETA','Honda','CG 160 Titan',2024,'AB527D23','9C2KC235836823456','Preta',15000,'Veículo utilizado para trabalho.','ATIVO','2026-08-13 12:33:18'),(8,2,'VAN','Honda','CG 160 Titan',2024,'AB7dg23','9C567gd823456','Preta',15000,'Veículo utilizado para trabalho.','ATIVO','2026-08-13 12:35:38'),(9,1,'OUTRO','Honda','CG 160 Titan',2024,'Agfdsdg23','9Cfdaf3456','Preta',15000,'Veículo utilizado para trabalho.','ATIVO','2026-08-13 12:36:11');
/*!40000 ALTER TABLE `veiculos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-08-13 17:34:04
