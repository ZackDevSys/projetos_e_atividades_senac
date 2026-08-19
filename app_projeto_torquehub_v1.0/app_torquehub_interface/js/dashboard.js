/*
 * =========================================================
 * TORQUEHUB - DASHBOARD
 * =========================================================
 */


/*
 * =========================================================
 * USUÁRIO LOGADO
 * =========================================================
 */

const usuarioSalvo =
    localStorage.getItem("torquehub_usuario");


/*
 * Se não existir usuário salvo,
 * volta para o login.
 */

if (!usuarioSalvo) {

    window.location.href = "login.html";

} else {

    const usuario =
        JSON.parse(usuarioSalvo);


    /*
     * =====================================================
     * DADOS DO USUÁRIO
     * =====================================================
     */

    const saudacao =
        document.getElementById("saudacao");

    if (saudacao) {

        saudacao.textContent =
            `Bem-vindo, ${usuario.nome}!`;
    }


    /*
     * Nome do usuário
     */

    const nomeUsuario =
        document.getElementById("nome-usuario");

    if (nomeUsuario) {

        nomeUsuario.textContent =
            usuario.nome;
    }


    /*
     * Perfil do usuário
     */

    const perfilUsuario =
        document.getElementById("perfil-usuario");

    if (perfilUsuario) {

        perfilUsuario.textContent =
            usuario.perfil;
    }


    /*
     * =====================================================
     * AVATAR
     * =====================================================
     */

    const avatar =
        document.querySelector(".usuario-avatar");

    if (avatar && usuario.nome) {

        avatar.textContent =
            usuario.nome
                .charAt(0)
                .toUpperCase();
    }


    /*
     * =====================================================
     * CARREGAR DASHBOARD
     * =====================================================
     */

    carregarDashboard();


    /*
     * =====================================================
     * LOGOUT
     * =====================================================
     */

    const botaoSair =
        document.getElementById("botao-sair");

    if (botaoSair) {

        botaoSair.addEventListener(
            "click",
            function () {

                localStorage.removeItem(
                    "torquehub_usuario"
                );

                window.location.href =
                    "login.html";
            }
        );
    }

}


/*
 * =========================================================
 * CARREGAR DADOS DO DASHBOARD
 * =========================================================
 */

async function carregarDashboard() {

    try {

        /*
         * Faz todas as consultas simultaneamente.
         */

        const [
            clientes,
            veiculos,
            ordens,
            pecas
        ] = await Promise.all([

            fazerRequisicao("/clientes/"),

            fazerRequisicao("/veiculos/"),

            fazerRequisicao("/ordens-servico/"),

            fazerRequisicao("/pecas/")

        ]);


        /*
         * =================================================
         * DEBUG
         * =================================================
         *
         * Mantemos estes logs por enquanto para verificar
         * exatamente o que a API está enviando.
         */

        console.log(
            "Clientes recebidos:",
            clientes
        );

        console.log(
            "Veículos recebidos:",
            veiculos
        );

        console.log(
            "Ordens recebidas:",
            ordens
        );

        console.log(
            "Peças recebidas:",
            pecas
        );


        /*
         * =================================================
         * CLIENTES ATIVOS
         * =================================================
         */

        atualizarClientesAtivos(
            clientes
        );


        /*
         * =================================================
         * VEÍCULOS ATIVOS
         * =================================================
         */

        atualizarVeiculosAtivos(
            veiculos
        );


        /*
         * =================================================
         * ORDENS ABERTAS
         * =================================================
         */

        atualizarOrdensAbertas(
            ordens
        );


        /*
         * =================================================
         * PEÇAS DISPONÍVEIS
         * =================================================
         */

        atualizarPecasDisponiveis(
            pecas
        );


    } catch (erro) {

        console.error(
            "Erro ao carregar dados do dashboard:",
            erro
        );

    }

}


/*
 * =========================================================
 * OBTER DADOS DA RESPOSTA DA API
 * =========================================================
 *
 * A API do TorqueHub normalmente retorna:
 *
 * {
 *     dados: [...]
 * }
 *
 * Esta função também aceita um array direto.
 *
 * =========================================================
 */

function obterDados(resultado) {

    if (
        resultado &&
        Array.isArray(resultado.dados)
    ) {

        return resultado.dados;
    }


    if (Array.isArray(resultado)) {

        return resultado;
    }


    console.warn(
        "A API não retornou uma lista de dados:",
        resultado
    );


    return [];
}


/*
 * =========================================================
 * NORMALIZAR STATUS
 * =========================================================
 *
 * Evita problemas como:
 *
 * "ativo"
 * "ATIVO"
 * " Ativo "
 *
 * Todos passam a ser:
 *
 * "ATIVO"
 *
 * =========================================================
 */

function normalizarStatus(status) {

    if (
        status === null ||
        status === undefined
    ) {

        return "";
    }


    return String(status)
        .trim()
        .toUpperCase()
        .normalize("NFD")
        .replace(/[\u0300-\u036f]/g, "")
        .replace(/\s+/g, "_");
}


/*
 * =========================================================
 * CLIENTES ATIVOS
 * =========================================================
 *
 * Conta somente clientes com:
 *
 * status = ATIVO
 *
 * =========================================================
 */

function atualizarClientesAtivos(resultado) {

    const elemento =
        document.getElementById("total-clientes");


    if (!elemento) {

        return;
    }


    const clientes =
        obterDados(resultado);


    console.log(
        "Quantidade de clientes recebidos:",
        clientes.length
    );


    const clientesAtivos =
        clientes.filter(function (cliente) {

            const status =
                normalizarStatus(
                    cliente.status
                );


            console.log(
                "Cliente:",
                cliente.nome,
                "| Status:",
                cliente.status,
                "| Normalizado:",
                status
            );


            return status === "ATIVO";

        });


    console.log(
        "Clientes ativos:",
        clientesAtivos.length
    );


    elemento.textContent =
        clientesAtivos.length;
}


/*
 * =========================================================
 * VEÍCULOS ATIVOS
 * =========================================================
 *
 * Conta somente veículos com:
 *
 * status = ATIVO
 *
 * =========================================================
 */

function atualizarVeiculosAtivos(resultado) {

    const elemento =
        document.getElementById("total-veiculos");


    if (!elemento) {

        return;
    }


    const veiculos =
        obterDados(resultado);


    const veiculosAtivos =
        veiculos.filter(function (veiculo) {

            const status =
                normalizarStatus(
                    veiculo.status
                );


            return status === "ATIVO";

        });


    elemento.textContent =
        veiculosAtivos.length;
}


/*
 * =========================================================
 * PEÇAS DISPONÍVEIS
 * =========================================================
 *
 * Uma peça será contabilizada somente quando:
 *
 * 1. status = ATIVO
 *
 * E
 *
 * 2. estoque_atual > 0
 *
 * =========================================================
 */

function atualizarPecasDisponiveis(resultado) {

    const elemento =
        document.getElementById("total-pecas");


    if (!elemento) {

        return;
    }


    const pecas =
        obterDados(resultado);


    const pecasDisponiveis =
        pecas.filter(function (peca) {

            const status =
                normalizarStatus(
                    peca.status
                );


            const quantidade =
                Number(
                    peca.estoque_atual || 0
                );


            return (
                status === "ATIVO" &&
                quantidade > 0
            );

        });


    elemento.textContent =
        pecasDisponiveis.length;
}


/*
 * =========================================================
 * ORDENS DE SERVIÇO ABERTAS
 * =========================================================
 *
 * São consideradas abertas:
 *
 * ABERTA
 * EM_ANALISE
 * AGUARDANDO_APROVACAO
 * EM_MANUTENCAO
 * AGUARDANDO_PECA
 *
 * Não entram:
 *
 * ENTREGUE
 * CANCELADA
 * FINALIZADA
 *
 * =========================================================
 */

function atualizarOrdensAbertas(resultado) {

    const elemento =
        document.getElementById("total-ordens");


    if (!elemento) {

        return;
    }


    const ordens =
        obterDados(resultado);


    const statusAbertos = [

        "ABERTA",

        "EM_ANALISE",

        "AGUARDANDO_APROVACAO",

        "EM_MANUTENCAO",

        "AGUARDANDO_PECA"

    ];


    const ordensAbertas =
        ordens.filter(function (ordem) {

            const status =
                normalizarStatus(
                    ordem.status
                );


            return statusAbertos.includes(
                status
            );

        });


    console.log(
        "Ordens abertas:",
        ordensAbertas.length
    );


    elemento.textContent =
        ordensAbertas.length;
}