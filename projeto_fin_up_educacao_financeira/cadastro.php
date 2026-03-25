<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FinUp | Cadastro</title>
    <link rel="stylesheet" href="css/login_cadastro.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>

<body>

    <!-- EFEITOS DE FUNDO -->
    <div class="glow-blue"></div>
    <div class="glow-orange"></div>

    <div class="login-wrapper">

        <!-- BOTÃO VOLTAR -->
        <a href="index.html" class="btn-back">← Voltar</a>

        <!-- LADO ESQUERDO -->
        <div class="login-left">
            <h1>Cria sua conta e deixa comigo…</h1>
            <h2> eu te ajudo a <span>dominar seu dinheiro </span>💸</h2>

            <img src="img/porquinho_fin_png.png" alt="FinUp">
        </div>

        <!-- FORMULÁRIO -->
        <div class="container">
            <div class="logo">
                <span>Fin</span><span>Up</span>
            </div>

            <!-- melhoria: mensagem de erro dinâmica que aparece quando o cadastro falha -->
            <p id="mensagemCadastro"></p>

            <form action="bd_connect/cadastrar.php" method="POST" onsubmit="return validarFormulario()">

                <!-- NOME DE USUÁRIO -->
                <div class="input-group">
                    <input type="text" name="usuario" id="usuario" placeholder="Nome de usuário" required>
                </div>

                <!-- EMAIL -->
                <div class="input-group">
                    <input type="email" name="email" id="email" placeholder="Email" required>
                </div>

                <!-- SENHA -->
                <div class="input-group senha-group">
                    <input type="password" name="senha" id="senha" placeholder="Senha" required>

                    <span class="toggle-senha" onclick="mostrarSenha(this)">👁</span>
                </div>

                <!-- CONFIRMAR SENHA -->
                <div class="input-group senha-group">
                    <input type="password" id="confirmarSenha" placeholder="Confirmar senha" required>
                    <span class="toggle-senha" onclick="mostrarSenha(this)">👁</span>
                </div>

                <button class="btn-primary">
                    Criar Conta
                </button>

            </form>

            <p class="register">
                Já tem uma conta?
                <a href="login.php">Entrar</a>
            </p>

            <div class="footer">
                © 2026 FinUp - Educação Financeira Inteligente
            </div>
        </div>
    </div>

    <script src="js/script.js"></script>

</body>

</html>