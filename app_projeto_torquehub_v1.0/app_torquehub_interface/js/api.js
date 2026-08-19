/* =========================================================
   TORQUEHUB
   CONEXÃO COM A API
========================================================= */

const API_URL = "http://localhost:5000/api";


/* =========================================================
   FUNÇÃO PRINCIPAL DE REQUISIÇÃO
========================================================= */

async function fazerRequisicao(endpoint, opcoes = {}) {

    const configuracao = {

        headers: {
            "Content-Type": "application/json",
            ...(opcoes.headers || {})
        },

        ...opcoes

    };


    try {

        const resposta = await fetch(
            `${API_URL}${endpoint}`,
            configuracao
        );


        let dados = null;


        /*
         * Algumas respostas da API podem não possuir JSON.
         * Por isso verificamos antes de tentar converter.
         */

        const tipoConteudo =
            resposta.headers.get("content-type");


        if (
            tipoConteudo &&
            tipoConteudo.includes("application/json")
        ) {

            dados = await resposta.json();

        }


        /*
         * Se a API retornar erro
         */

        if (!resposta.ok) {

            throw new Error(
                dados?.mensagem ||
                dados?.erro ||
                `Erro HTTP ${resposta.status}`
            );

        }


        return dados;


    } catch (erro) {

        console.error(
            "Erro na comunicação com a API:",
            erro
        );

        throw erro;

    }

}


/* =========================================================
   GET
========================================================= */

async function apiGet(endpoint) {

    return await fazerRequisicao(
        endpoint,
        {
            method: "GET"
        }
    );

}


/* =========================================================
   POST
========================================================= */

async function apiPost(endpoint, dados) {

    return await fazerRequisicao(
        endpoint,
        {
            method: "POST",

            body: JSON.stringify(dados)
        }
    );

}


/* =========================================================
   PUT
========================================================= */

async function apiPut(endpoint, dados) {

    return await fazerRequisicao(
        endpoint,
        {
            method: "PUT",

            body: JSON.stringify(dados)
        }
    );

}


/* =========================================================
   DELETE
========================================================= */

async function apiDel(endpoint) {

    return await fazerRequisicao(
        endpoint,
        {
            method: "DELETE"
        }
    );

}