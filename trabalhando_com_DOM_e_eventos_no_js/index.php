<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/style.css">
    <title>Controle de Estoque</title>
</head>

<?php
$erro = $_GET['erro'] ?? null;
?>

<body>

    <div class="content">
        <div class="img_logo">
            <img class="logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png" alt="">
        </div>

        <div class="container">
            <h1>Gestão de Estoque</h1>

            <form action="php-action/login.php" method="POST">

                <select id="usuario" name="perfil">
                    <option value="">Selecione o tipo de usuário</option>
                    <option value="vendedor">Vendedor</option>
                    <option value="estoquista">Estoquista</option>
                    <option value="admin">Admin</option>
                </select>

                <input type="password" name="senha" placeholder="Senha">

                <button type="submit">Entrar</button>

            </form>

            <?php if ($erro === '1'): ?>
                <p class="msg-error" id="msgErro">
                    Usuário ou senha inválidos!
                </p>
            <?php elseif ($erro === 'perfil'): ?>
                <p class="msg-error" id="msgErro">
                    Selecione um perfil de usuário!
                </p>
            <?php endif; ?>

        </div>
    </div>

    <script src="js/script.js"></script>

</body>

</html>