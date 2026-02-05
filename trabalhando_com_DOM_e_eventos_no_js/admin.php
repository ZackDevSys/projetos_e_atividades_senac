<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin</title>
    <link rel="stylesheet" href="css/estoque.css">
</head>

<?php
session_start();

if (!isset($_SESSION['perfil']) || $_SESSION['perfil'] !== 'admin') {
    header('Location: vendas.php');
    exit;
}

include_once 'php-action/db_connect.php';

// Total de produtos
$totalProdutos = mysqli_fetch_row(
    mysqli_query($connect, "SELECT COUNT(*) FROM estoque")
)[0];

// Estoque total (kg)
$estoqueTotal = mysqli_fetch_row(
    mysqli_query($connect, "SELECT SUM(quantidade) FROM estoque")
)[0];

// Valor estimado do estoque
$valorEstoque = mysqli_fetch_row(
    mysqli_query($connect, "SELECT SUM(preco * quantidade) FROM estoque")
)[0];

// Vendas hoje
$vendasHoje = mysqli_fetch_row(
    mysqli_query($connect, "SELECT SUM(total) FROM vendas WHERE DATE(data_venda)=CURDATE()")
)[0];
?>

<body>
    <main class="estoque-wrapper">

        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Painel Administrativo</h1>
            </div>
        </div>

        <div class="dashboard">
            <div class="card">
                📦 Produtos
                <strong><?= $totalProdutos ?></strong>
            </div>

            <div class="card">
                ⚖️ Estoque Total
                <strong><?= number_format($estoqueTotal, 2, ',', '.') ?> kg</strong>
            </div>

            <div class="card">
                💰 Valor em Estoque
                <strong>R$ <?= number_format($valorEstoque, 2, ',', '.') ?></strong>
            </div>

            <div class="card destaque">
                📊 Vendas Hoje
                <strong>R$ <?= number_format($vendasHoje ?? 0, 2, ',', '.') ?></strong>
            </div>
        </div>

        <div class="acoes-admin">
            <div>
                <a href="estoque.php"><button class="btn-padrao">Gerenciar Estoque</button></a>
                <a href="vendas.php"><button class="btn-padrao">Registrar Venda</button></a>
                <a href="relatorio_vendas.php"><button class="btn-padrao">Relatório de Vendas</button></a>
            </div>

            <button class="btn-sair" onclick="abrirModalSair()">Sair do Sistema</button>
        </div>

    </main>

    <!-- MODAL SAIR DO SISTEMA -->
    <div id="modalSair" class="modal">
        <div class="modal-content">
            <h3>Sair do Sistema</h3>
            <p>Tem certeza que deseja sair?</p>

            <div class="modal-actions">
                <button onclick="fecharModalSair()" class="btn-cancelar">Cancelar</button>
                <a href="index.php">
                    <button class="btn-excluir">Sair</button>
                </a>
            </div>
        </div>
    </div>

    <script src="js/script.js"></script>

</body>

</html>