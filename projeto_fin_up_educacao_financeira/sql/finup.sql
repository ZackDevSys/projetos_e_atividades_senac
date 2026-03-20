-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 20-Mar-2026 às 03:05
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
-- Banco de dados: `finup`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `transacoes`
--

CREATE TABLE `transacoes` (
  `id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `descricao` varchar(255) DEFAULT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  `valor` decimal(10,2) DEFAULT NULL,
  `fixa` varchar(20) DEFAULT NULL,
  `data_criacao` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `transacoes`
--

INSERT INTO `transacoes` (`id`, `usuario_id`, `categoria`, `descricao`, `tipo`, `valor`, `fixa`, `data_criacao`) VALUES
(1, 1, 'moradia', 'Aluguel', 'despesa', 570.00, 'fixa', '2026-03-11 16:57:08'),
(2, 1, 'trabalho', 'CLT', 'receita', 1618.00, 'fixa', '2026-03-11 17:22:11'),
(3, 1, 'transporte', 'Onibus', 'despesa', 254.00, 'fixa', '2026-03-11 17:37:08'),
(6, 1, 'trabalho', 'Freelance', 'receita', 2200.00, 'nao-fixa', '2026-03-19 18:10:32'),
(7, 1, 'outros', 'Desapego', 'receita', 620.00, 'nao-fixa', '2026-03-19 18:34:39'),
(8, 1, 'transporte', 'Uber', 'despesa', 175.00, 'nao-fixa', '2026-03-19 19:25:25');

-- --------------------------------------------------------

--
-- Estrutura da tabela `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `senha` varchar(255) NOT NULL,
  `data_cadastro` timestamp NOT NULL DEFAULT current_timestamp(),
  `token` varchar(255) DEFAULT NULL,
  `verificado` tinyint(1) DEFAULT 0,
  `criado_em` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `usuarios`
--

INSERT INTO `usuarios` (`id`, `usuario`, `email`, `senha`, `data_cadastro`, `token`, `verificado`, `criado_em`) VALUES
(1, 'Isaac', 'isaactcosta20142@gmail.com', '$2y$10$sHfzXMUHhYuXlP78eCWTO.RJPzkUcrB44XXbVZsgZH4w5lKc.43Ca', '2026-03-07 02:01:07', NULL, 1, '2026-03-07 03:28:49'),
(2, 'Boyka', 'isaactcosta2014@gmail.com', '$2y$10$EY8jb/u8gP4PVRUaZuyn3.FpP7w4mOx7r2yiPlS9/um0bUAkNBx7.', '2026-03-07 03:11:41', '1fe200cd91691afc5ee2d153cbd06862a418cda48e56861c57290ff42c81ae3f', 0, '2026-03-07 03:28:49');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `transacoes`
--
ALTER TABLE `transacoes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `usuario_id` (`usuario_id`);

--
-- Índices para tabela `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `transacoes`
--
ALTER TABLE `transacoes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de tabela `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restrições para despejos de tabelas
--

--
-- Limitadores para a tabela `transacoes`
--
ALTER TABLE `transacoes`
  ADD CONSTRAINT `transacoes_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
