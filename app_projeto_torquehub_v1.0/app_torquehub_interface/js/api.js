const API_URL = "http://localhost:5000/api";

async function fazerRequisicao(endpoint, opcoes = {}) {

    const configuracao = {
        headers: {
            "Content-Type": "application/json",
            ...(opcoes.headers || {})
        },
        ...opcoes
    };

    const resposta = await fetch(
        `${API_URL}${endpoint}`,
        configuracao
    );

    const dados = await resposta.json();

    if (!resposta.ok) {
        throw new Error(
            dados.mensagem || "Erro ao realizar requisição."
        );
    }

    return dados;
}