<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FinUp | Login</title>
    <link rel="stylesheet" href="css/login_cadastro.css">
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
</head>

<body>

    <!-- EFEITOS DE FUNDO -->
    <div class="glow-blue"></div>
    <div class="glow-orange"></div>

    <div class="login-wrapper">
        <!-- BOTÃO VOLTAR -->
        <!-- melhoria: botão simples que retorna para página anterior -->
        <a href="index.html" class="btn-back">← Voltar</a>

        <!-- LADO ESQUERDO -->
        <div class="login-left">

            <h1>Que bom te ver de novo! 👋</h1>
            <h2>Vamos continuar sua <span>evolução financeira ?</span></h2>

            <img src="img/porquinho_fin_png.png" alt="FinUp">

        </div>

        <!-- FORMULÁRIO -->
        <div class="container">

            <div class="logo">
                <span>Fin</span><span>Up</span>
            </div>

            <!-- melhoria: mensagem de erro dinâmica que aparece quando o login falha -->
            <p id="mensagemLogin"></p>

            <form action="bd_connect/login.php" method="POST">

                <div class="input-group">
                    <input type="email" name="email" placeholder="Email" required>
                </div>

                <div class="input-group senha-group">
                    <input type="password" name="senha" id="senha" placeholder="Senha" required>

                    <span class="toggle-senha" onclick="mostrarSenha(this)">👁</span>
                </div>

                <div class="remember">

                    <label class="checkbox">
                        <input type="checkbox"> Lembrar senha
                    </label>

                    <a href="#" class="forgot-password">Esqueceu a senha?</a>

                </div>

                <button type="submit" class="btn-primary">Entrar na Plataforma</button>

            </form>

            <div class="reenviar-area">

                <!-- melhoria: mensagem de sucesso ou erro que aparece após tentar reenviar o email de verificação -->
                <p id="mensagemReenvio"></p>

                <p class="reenviar-texto">
                    <span class="texto-fixo">Não recebeu o email de verificação?</span>
                    <span class="reenviar-toggle">Reenviar</span>
                </p>

                <form class="reenviar-box" id="formReenviar" action="bd_connect/reenviar_verificacao.php" method="POST">

                    <div id="inputGroup" class="input-group">
                        <input type="email" name="email" placeholder="Digite seu email" required>
                    </div>

                    <button type="submit" class="btn-secondary">
                        Reenviar email de verificação
                    </button>

                </form>

            </div>

            <p class="register">
                Não tem uma conta?
                <a href="cadastro.php">Cadastrar</a>
            </p>

            <div class="footer">
                © 2026 FinUp - Educação Financeira Inteligente
            </div>
        </div>
    </div>

    <script src="js/script.js">

    </script>

</body>

</html>