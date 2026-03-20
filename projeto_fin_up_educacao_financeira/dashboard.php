<?php
session_start();

if (!isset($_SESSION['usuario_id'])) {
    header("Location: login.html");
    exit();
}

// impedir cache
header("Cache-Control: no-cache, no-store, must-revalidate");
header("Pragma: no-cache");
header("Expires: 0");
?>

<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FinUp Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link rel="stylesheet" href="css/stilo.css">
</head>

<body>

    <div class="glow-blue"></div>
    <div class="glow-orange"></div>

    <button id="btnNovaTransacao" class="btn-flutuante">
        <i class="fa-solid fa-plus"></i>
    </button>

    <div class="container">

        <div class="header">
            <div class="logo">Fin<span>Up</span></div>

            <div class="user-area">
                <span class="bem-vindo">
                    Bem-vindo, <strong><?php echo $_SESSION['usuario_nome']; ?></strong> 👋
                </span>

                <a href="#" class="btn-sair" onclick="abrirModalLogout()">
                    <i class="fa-solid fa-right-from-bracket"></i> Sair
                </a>
            </div>
        </div>

        <h2>Dashboard Financeiro</h2>

        <!-- CARDS -->

        <div class="cards">

            <div class="card">
                <h4>Saldo</h4>
                <span id="saldo">R$ 0</span>
            </div>

            <div class="card">
                <h4>Receitas</h4>
                <span class="green" id="receitas">R$ 0</span>
            </div>

            <div class="card">
                <h4>Despesas</h4>
                <span class="red" id="despesas">R$ 0</span>
            </div>

        </div>

        <!-- GRÁFICOS -->

        <div class="graficos-container">
            <div class="grafico-box">
                <h2>Receitas</h2>
                <canvas id="graficoReceitas"></canvas>
            </div>

            <div class="grafico-box">
                <h2>Despesas</h2>
                <canvas id="grafico"></canvas>
            </div>
        </div>

        <div class="legenda-grafico">
            <span>
                <div class="cor trabalho"></div> Trabalho
            </span>
            <span>
                <div class="cor moradia"></div> Moradia
            </span>
            <span>
                <div class="cor educacao"></div> Educação
            </span>
            <span>
                <div class="cor investimento"></div> Investimento
            </span>
            <span>
                <div class="cor alimentacao"></div> Alimentação
            </span>
            <span>
                <div class="cor transporte"></div> Transporte
            </span>
            <span>
                <div class="cor outros"></div> Outros
            </span>
        </div>

        <!-- LISTA -->

        <div class="list">
            <h3>Transações</h3>

            <div class="lista-header">
                <span>Data</span>
                <span>Categoria</span>
                <span>Descrição</span>
                <span>Tipo</span>
                <span>Valor</span>
                <span>Ações</span>
            </div>

            <div id="lista"></div>
        </div>

        <!-- SIMULADORES -->

        <div class="simulators">

            <div class="sim-box">

                <h3>Simulador CDI</h3>

                <input id="invest" placeholder="Valor investido">

                <input id="meses" placeholder="Meses">

                <button class="btn-secondary" onclick="simularCDI()">Simular</button>

                <div class="result" id="cdiResultado"></div>

            </div>

            <div class="sim-box">

                <h3>Simulador Juros Cartão</h3>

                <input id="divida" placeholder="Valor da dívida">

                <input id="juros" placeholder="% juros ao mês">

                <input id="tempo" placeholder="Meses">

                <button class="btn-secondary" onclick="simularJuros()">Simular</button>

                <div class="result" id="jurosResultado"></div>

            </div>

        </div>

        <div class="alert" id="alerta">
            ⚠️ Atenção: seus gastos já ultrapassaram suas receitas.
        </div>

    </div>

    <div id="modalTransacao" class="modal">
        <div class="modal-conteudo">

            <!-- FORM -->

            <div class="form">
                <h3>Nova Transação</h3>

                <!-- CATEGORIA -->
                <select id="categoria">
                    <option value="trabalho">Trabalho</option>
                    <option value="moradia">Moradia</option>
                    <option value="educacao">Educação</option>
                    <option value="investimento">Investimento</option>
                    <option value="alimentacao">Alimentação</option>
                    <option value="transporte">Transporte</option>
                    <option value="outros">Outros</option>
                </select>

                <!-- DESCRIÇÃO -->
                <input id="desc" placeholder="Descrição">

                <!-- VALOR -->
                <input id="valor" type="number" placeholder="Valor">

                <!-- TIPO -->
                <select id="tipo">
                    <option value="receita">Receita</option>
                    <option value="despesa">Despesa</option>
                </select>

                <!-- FIXA OU NÃO -->
                <select id="fixo">
                    <option value="fixa">Fixa</option>
                    <option value="nao-fixa">Não Fixa</option>
                </select>

                <button id="btn-salvar" onclick="salvarTransacao()">Salvar</button>
                <button class="btn-voltar" onclick="fecharModal()">Cancelar</button>

            </div>
        </div>
    </div>

    <!-- MODAL CONFIRMAR EXCLUSÃO -->

    <div id="modalExcluir" class="modal">
        <div class="modal-conteudo modal-excluir">
            <h3>Excluir Transação</h3>

            <p>Tem certeza que deseja excluir esta transação?</p>

            <div class="botoes-modal">

                <button class="btn-danger" onclick="confirmarExcluir()">
                    Excluir
                </button>

                <button class="btn-fechar-modal" onclick="fecharModalExcluir()">
                    Cancelar
                </button>
            </div>
        </div>
    </div>

    <!-- MODAL CONFIRMAR LOGOUT -->

    <div id="modalLogout" class="modal">
        <div class="modal-conteudo modal-excluir">

            <h3>Sair da conta</h3>
            <p>Deseja realmente sair do FinUp?</p>

            <div class="botoes-modal">
                <button class="btn-fechar-modal" onclick="fecharModalLogout()">
                    Cancelar
                </button>

                <button class="btn-danger" onclick="confirmarLogout()">
                    Sair
                </button>
            </div>
        </div>
    </div>

    <script src="js/script.js"></script>

</body>

</html>