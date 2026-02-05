<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Relatório de Vendas</title>
    <link rel="stylesheet" href="css/estoque.css">
</head>

<?php
include_once 'php-action/db_connect.php';

$dataInicio = $_GET['inicio'] ?? '';
$dataFim = $_GET['fim'] ?? '';

$filtro = '';
if ($dataInicio && $dataFim) {
    $filtro = "WHERE DATE(data_venda) BETWEEN '$dataInicio' AND '$dataFim'";
}

$sql = "SELECT * FROM vendas $filtro ORDER BY data_venda DESC";
$resultado = mysqli_query($connect, $sql);

$totalRegistros = mysqli_num_rows($resultado);
?>

<body>
    <main class="estoque-wrapper">

        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Relatório de Vendas</h1>
            </div>

            <button class="btn-padrao" onclick="window.location.href='admin.php'">← Voltar</button>
        </div>

        <form class="estoque-filtro" method="GET">
            <input type="date" name="inicio" value="<?= $dataInicio ?>">
            <input type="date" name="fim" value="<?= $dataFim ?>">
            <button>Filtrar</button>
        </form>

        <table>
            <thead>
                <tr>
                    <th>Produto</th>
                    <th>Qtd (kg)</th>
                    <th>Total</th>
                    <th>Data</th>
                </tr>
            </thead>
            <tbody>
                <?php if ($totalRegistros > 0): ?>
                    <?php while ($v = mysqli_fetch_assoc($resultado)): ?>
                        <tr>
                            <td><?= $v['nome_produto'] ?></td>
                            <td><?= number_format($v['quantidade'], 2, ',', '.') ?> kg</td>
                            <td>R$ <?= number_format($v['total'], 2, ',', '.') ?></td>
                            <td><?= date('d/m/Y H:i', strtotime($v['data_venda'])) ?></td>
                        </tr>
                    <?php endwhile; ?>
                <?php else: ?>
                    <tr>
                        <td colspan="4" style="text-align:center; padding: 20px;">
                            Não há vendas registradas entre essas datas
                        </td>
                    </tr>
                <?php endif; ?>
            </tbody>
        </table>

    </main>
</body>

</html>