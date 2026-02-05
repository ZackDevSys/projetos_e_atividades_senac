<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Novo Produto</title>
    <link rel="stylesheet" href="css/novo_produto.css">
</head>

<?php
//***************CONEXÃO***************
include_once 'php-action/db_connect.php';
?>

<body>

    <main class="estoque-wrapper">

        <!-- Cabeçalho -->
        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Cadastrar Produto</h1>
            </div>

            <a href="estoque.php">
                <button class="btn-voltar">← Voltar</button>
            </a>
        </div>

        <!-- Formulário -->
        <form class="form-produto" action="php-action/create.php" method="POST">

            <div class="form-group">
                <label>Nome do Produto</label>
                <input type="text" name="nome_produto" required>
            </div>

            <div class="form-group">
                <label>Categoria</label>
                <select name="categoria" required>
                    <option value="">Selecione</option>
                    <option value="Grãos">Grãos</option>
                    <option value="Cereais">Cereais</option>
                    <option value="Farinhas">Farinhas</option>
                </select>
            </div>

            <div class="form-row">
                <div class="form-group">
                    <label>Preço por Kg (R$)</label>
                    <input type="number" step="0.01" name="preco" required>
                </div>

                <div class="form-group">
                    <label>Quantidade em Estoque (Kg)</label>
                    <input type="number" step="0.01" name="quantidade" required>
                </div>
            </div>

            <button type="submit" class="btn-cadastrar">Salvar Produto</button>

        </form>

    </main>

</body>

</html>