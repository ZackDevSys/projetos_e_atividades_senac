<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Editar Produto</title>
    <link rel="stylesheet" href="css/novo_produto.css">
</head>

<?php
include_once 'php-action/db_connect.php';

if (!isset($_GET['id'])) {
    header('Location: estoque.php');
    exit;
}

$idcodigo = intval($_GET['id']);

$sql = "SELECT * FROM estoque WHERE idcodigo = $idcodigo";
$resultado = mysqli_query($connect, $sql);
$dados = mysqli_fetch_assoc($resultado);

if (!$dados) {
    header('Location: estoque.php?msg=erro');
    exit;
}
?>

<body>

    <main class="estoque-wrapper">

        <!-- Cabeçalho -->
        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Editar Produto</h1>
            </div>

            <a href="estoque.php">
                <button class="btn-voltar">← Voltar</button>
            </a>
        </div>

        <!-- Formulário -->
        <form class="form-produto" action="php-action/update.php" method="POST">

            <input type="hidden" name="idcodigo" value="<?php echo $dados['idcodigo']; ?>">

            <div class="form-group">
                <label>Nome do Produto</label>
                <input type="text" name="nome_produto"
                    value="<?php echo $dados['nome_produto']; ?>" required>
            </div>

            <div class="form-group">
                <label>Categoria</label>
                <select name="categoria" required>
                    <option value="Grãos" <?= $dados['categoria'] == 'Grãos' ? 'selected' : '' ?>>Grãos</option>
                    <option value="Cereais" <?= $dados['categoria'] == 'Cereais' ? 'selected' : '' ?>>Cereais</option>
                    <option value="Farinhas" <?= $dados['categoria'] == 'Farinhas' ? 'selected' : '' ?>>Farinhas</option>
                </select>
            </div>

            <div class="form-row">
                <div class="form-group">
                    <label>Preço por Kg (R$)</label>
                    <input type="number" step="0.01" name="preco"
                        value="<?php echo $dados['preco']; ?>" required>
                </div>

                <div class="form-group">
                    <label>Quantidade em Estoque (Kg)</label>
                    <input type="number" step="0.01" name="quantidade"
                        value="<?php echo $dados['quantidade']; ?>" required>
                </div>
            </div>

            <button type="submit" class="btn-editar">Atualizar Produto</button>

        </form>

    </main>

</body>

</html>