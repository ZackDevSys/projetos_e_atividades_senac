<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Registrar Venda</title>
    <link rel="stylesheet" href="css/estoque.css">
</head>

<?php
session_start();

if (
    !isset($_SESSION['perfil']) ||
    ($_SESSION['perfil'] !== 'admin' && $_SESSION['perfil'] !== 'vendedor')
) {
    header('Location: estoque.php');
    exit;
}

//***************CONEXÃO***************
include_once 'php-action/db_connect.php';
?>

<body>
    <main class="estoque-wrapper">

        <!-- Cabeçalho -->
        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Registrar Venda</h1>
            </div>

            <div>
                <?php if (isset($_SESSION['perfil']) && $_SESSION['perfil'] === 'admin'): ?>
                    <button class="btn-padrao" onclick="window.location.href='admin.php'">
                        ← Voltar
                    </button>
                <?php endif; ?>

                <?php if (isset($_SESSION['perfil']) && $_SESSION['perfil'] === 'vendedor'): ?>
                    <button class="btn-sair" onclick="abrirModalSair()">Sair do Sistema</button>
                <?php endif; ?>

            </div>
        </div>

        <!-- Mensagem -->
        <?php if (isset($_GET['msg_venda'])): ?>
            <div class="msg sucesso">
                <?= htmlspecialchars($_GET['msg_venda']) ?>
            </div>
        <?php endif; ?>

        <!-- Formulário de Venda -->
        <form class="form-venda" action="php-action/realizar_vendas.php" method="POST" id="formVenda">

            <div class="form-card">

                <div class="form-group">
                    <label for="produto">Produto</label>
                    <select name="codigo_produto" id="produto" required>
                        <option value="">Selecione o produto</option>
                        <?php
                        $sql = "SELECT idcodigo, nome_produto, preco, quantidade FROM estoque";
                        $res = mysqli_query($connect, $sql);
                        while ($p = mysqli_fetch_assoc($res)):
                        ?>
                            <option
                                value="<?= $p['idcodigo'] ?>"
                                data-preco="<?= $p['preco'] ?>"
                                data-estoque="<?= $p['quantidade'] ?>">
                                <?= $p['nome_produto'] ?> (<?= number_format($p['quantidade'], 2, ',', '.') ?> kg)
                            </option>
                        <?php endwhile; ?>
                    </select>
                </div>

                <div class="form-group">
                    <label for="quantidade">Quantidade (kg)</label>
                    <input type="number" step="0.01" min="0.01" id="quantidade" name="quantidade_venda" required>
                    <small id="msgErro" class="erro"></small>
                </div>

                <div class="form-group destaque-total">
                    <label>Total da Venda</label>
                    <input type="text" id="total" readonly>
                </div>

                <div class="form-actions">
                    <button type="submit" class="btn-salvar">Finalizar Venda</button>
                </div>

            </div>

        </form>

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