-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 05-Fev-2026 às 21:32
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `produtos`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `estoque`
--

CREATE TABLE `estoque` (
  `idcodigo` int(11) NOT NULL,
  `nome_produto` varchar(45) NOT NULL,
  `categoria` varchar(45) NOT NULL,
  `preco` double NOT NULL,
  `quantidade` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `estoque`
--

INSERT INTO `estoque` (`idcodigo`, `nome_produto`, `categoria`, `preco`, `quantidade`) VALUES
(4, 'Farinha de Trigo', 'Farinhas', 21, 205),
(6, 'Farinha de Mandioca', 'Farinhas', 12.2, 76.75),
(7, 'Canjiquinha', 'Grãos', 15.02, 227.75),
(8, 'Milho Verde', 'Grãos', 21.12, 125.24),
(9, 'Café', 'Grãos', 31.2, 125),
(10, 'Farinha de Rosca', 'Farinhas', 12.32, 250);

-- --------------------------------------------------------

--
-- Estrutura da tabela `vendas`
--

CREATE TABLE `vendas` (
  `id` int(11) NOT NULL,
  `codigo_produto` int(11) DEFAULT NULL,
  `nome_produto` varchar(100) DEFAULT NULL,
  `quantidade` double DEFAULT NULL,
  `preco_kg` double DEFAULT NULL,
  `total` double DEFAULT NULL,
  `data_venda` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Extraindo dados da tabela `vendas`
--

INSERT INTO `vendas` (`id`, `codigo_produto`, `nome_produto`, `quantidade`, `preco_kg`, `total`, `data_venda`) VALUES
(1, 9, 'Café', 45.5, 31.2, 1419.6, '2026-02-05 14:09:37'),
(2, 9, 'Café', 45, 31.2, 1404, '2026-02-05 14:09:54'),
(3, 6, 'Farinha de Mandioca', 25.5, 12.2, 311.1, '2026-02-05 14:12:13'),
(4, 7, 'Canjiquinha', 152.25, 15.02, 2286.795, '2026-02-05 14:37:56'),
(5, 7, 'Canjiquinha', 25, 15.02, 375.5, '2026-02-05 14:45:24'),
(6, 7, 'Canjiquinha', 15, 15.02, 225.3, '2026-02-05 14:46:16'),
(7, 4, 'Farinha de Trigo', 45, 21, 945, '2026-02-05 15:13:50'),
(8, 4, 'Farinha de Trigo', 25, 21, 525, '2026-02-05 15:28:13'),
(9, 4, 'Farinha de Trigo', 15, 21, 315, '2026-02-05 15:30:16'),
(10, 4, 'Farinha de Trigo', 120, 21, 2520, '2026-02-05 15:37:53'),
(11, 10, 'Farinha de Rosca', 100, 12.32, 1232, '2026-02-05 17:03:30'),
(12, 4, 'Farinha de Trigo', 45, 21, 945, '2026-02-05 17:27:41');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `estoque`
--
ALTER TABLE `estoque`
  ADD PRIMARY KEY (`idcodigo`);

--
-- Índices para tabela `vendas`
--
ALTER TABLE `vendas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `estoque`
--
ALTER TABLE `estoque`
  MODIFY `idcodigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `vendas`
--
ALTER TABLE `vendas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
