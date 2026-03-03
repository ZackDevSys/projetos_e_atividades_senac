<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/estoque.css">
    <title>Gestão de Estoque</title>
</head>

<?php
session_start();

if (
    !isset($_SESSION['perfil']) ||
    ($_SESSION['perfil'] !== 'admin' && $_SESSION['perfil'] !== 'estoquista')
) {
    header('Location: vendas.php');
    exit;
}

//***************CONEXÃO***************
include_once 'php-action/db_connect.php';
?>

<?php
//***************MENSAGENS***************
if (isset($_GET['msg'])):
    switch ($_GET['msg']):
        case 'sucesso_cadastro':
            echo '<div class="msg sucesso">✅  Produto cadastrado com sucesso !</div>';
            break;
        case 'sucesso_edicao':
            echo '<div class="msg sucesso">✏️  Produto atualizado com sucesso !</div>';
            break;
        case 'sucesso_exclusao':
            echo '<div class="msg sucesso">🗑️  Produto excluído com sucesso !</div>';
            break;
        case 'erro':
            echo '<div class="msg erro">❌  Ocorreu um erro. Tente novamente.</div>';
            break;
    endswitch;
endif;
?>

<body>

    <main class="estoque-wrapper">

        <!-- Cabeçalho -->
        <div class="estoque-header">
            <div class="header-left">
                <img class="img-logo" src="img/a2e5f86a-6255-4836-b898-486021542a62.png">
                <h1>Produtos em Estoque</h1>
            </div>

            <div>
                <?php if (isset($_SESSION['perfil']) && $_SESSION['perfil'] === 'admin'): ?>
                    <button class="btn-padrao" onclick="window.location.href='admin.php'">← Voltar</button>
                <?php endif; ?>

                <?php if (isset($_SESSION['perfil']) && $_SESSION['perfil'] === 'admin'): ?>
                    <a href="novo_produto.php"><button class="btn-padrao">Novo Produto</button></a>
                <?php endif; ?>

                <?php if (isset($_SESSION['perfil']) && $_SESSION['perfil'] === 'estoquista'): ?>
                    <button class="btn-sair" onclick="abrirModalSair()">Sair do Sistema</button>
                <?php endif; ?>

            </div>
        </div>

        <!-- Filtro -->
        <form class="estoque-filtro" method="GET">
            <input type="text" name="busca" placeholder="Buscar produto ou categoria..." value="<?= isset($_GET['busca']) ? htmlspecialchars($_GET['busca']) : '' ?>">
            <button type="submit">🔍</button>
        </form>

        <!-- Tabela -->
        <div class="tabela-container">
            <table>
                <thead>
                    <tr>
                        <th>Código</th>
                        <th>Produto</th>
                        <th>Categoria</th>
                        <th>Preço por Kg</th>
                        <th>Estoque (Kg)</th>
                        <th>Ações</th>
                    </tr>
                </thead>

                <tbody>
                    <?php
                    // Busca
                    $busca = '';

                    if (isset($_GET['busca'])) {
                        $busca = mysqli_real_escape_string($connect, $_GET['busca']);
                    }

                    // SQL base
                    $sql = "SELECT * FROM produtos";

                    // Aplica filtro se houver busca
                    if (!empty($busca)) {
                        $sql .= " WHERE nome_produto LIKE '%$busca%' OR categoria LIKE '%$busca%'";
                    }

                    $resultado = mysqli_query($connect, $sql);

                    // Caso não encontre resultados
                    if (mysqli_num_rows($resultado) == 0): ?>
                        <tr>
                            <td colspan="6" style="text-align:center; padding: 20px;">
                                Nenhum produto encontrado
                            </td>
                        </tr>
                    <?php endif; ?>

                    <?php while ($dados = mysqli_fetch_array($resultado)): ?>

                        <tr>
                            <th>
                                <?php echo 'PROD-' . str_pad($dados['idcodigo'], 4, '0', STR_PAD_LEFT); ?>
                            </th>
                            <th>
                                <?php echo $dados['nome_produto']; ?>
                            </th>
                            <th>
                                <?php echo $dados['categoria']; ?>
                            </th>
                            <th>R$
                                <?php echo number_format($dados['preco'], 2, ',', '.'); ?>/kg
                            </th>
                            <th>
                                <?php echo number_format($dados['quantidade'], 2, ',', '.'); ?> kg
                            </th>

                            <td class="acoes">
                                <button class="editar"
                                    onclick="window.location.href='editar_produto.php?id=<?php echo $dados['idcodigo']; ?>'">
                                    ✏️
                                </button>

                                <button class="excluir"
                                    onclick="abrirModal(<?php echo $dados['idcodigo']; ?>)">
                                    🗑️
                                </button>
                            </td>
                        </tr>

                    <?php endwhile; ?>

                </tbody>
            </table>
        </div>

    </main>

    <!-- MODAL CONFIRMAÇÃO -->
    <div id="modalExcluir" class="modal">
        <div class="modal-content">
            <h3>Confirmar Exclusão</h3>
            <p>Tem certeza que deseja excluir este produto?</p>

            <div class="modal-actions">
                <button onclick="fecharModal()" class="btn-cancelar">Cancelar</button>
                <a id="linkExcluir" href="#">
                    <button name="btn-excluir" class="btn-excluir">Excluir</button>
                </a>
            </div>
        </div>
    </div>

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