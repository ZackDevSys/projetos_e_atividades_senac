let indexEditando = null
let indexExcluir = null
let transacoes = []

/* =========================
VALIDAR FORMULÁRIO DE CADASTRO
========================= */

function validarFormulario() {
    let senha = document.getElementById("senha").value;
    let confirmar = document.getElementById("confirmarSenha").value;
    let msg = document.getElementById("mensagemCadastro");

    if (!msg) return true;

    if (senha !== confirmar) {
        msg.innerText = "As senhas não coincidem !";
        msg.classList.add("mensagem-erro");
        msg.style.display = "block";
        autoSumir(msg);
        return false;
    }

    msg.innerText = "";
    msg.style.display = "none";
    return true;
}

/* =========================
RODAR APÓS CARREGAR
========================= */

document.addEventListener("DOMContentLoaded", () => {

    const params = new URLSearchParams(window.location.search);
    const erro = params.get("erro");
    const sucesso = params.get("sucesso");

    /* =========================
    LOGIN
    ========================= */

    const msgLogin = document.getElementById("mensagemLogin");

    if (msgLogin) {

        msgLogin.style.display = "none";

        if (erro || sucesso) {
            msgLogin.style.display = "block";

            autoSumir(msgLogin);
        }

        if (erro === "email_nao_existe") {
            msgLogin.innerText = "Esse email não está cadastrado !";
            msgLogin.classList.add("mensagem-erro");
        }

        if (erro === "senha_incorreta") {
            msgLogin.innerText = "Senha incorreta !";
            msgLogin.classList.add("mensagem-erro");
        }

        if (erro === "nao_verificado") {
            msgLogin.innerText = "Confirme seu email antes de entrar.";
            msgLogin.classList.add("mensagem-erro");
        }

        if (sucesso === "verifique_email") {
            msgLogin.innerText = "Cadastro feito! Verifique seu email.";
            msgLogin.classList.add("mensagem-sucesso");
        }
    }

    if (sucesso === "email_reenviado") {
        msgLogin.innerText = "Email reenviado com sucesso 📩";
        msgLogin.classList.add("mensagem-sucesso");
    }

    if (erro === "erro_reenvio") {
        msgLogin.innerText = "Erro ao reenviar email !";
        msgLogin.classList.add("mensagem-erro");
    }

    if (sucesso === "ja_verificado") {
        msgLogin.innerText = "Essa conta já está verificada !";
        msgLogin.classList.add("mensagem-sucesso");
    }

    /* =========================
    CADASTRO
    ========================= */

    const msgCadastro = document.getElementById("mensagemCadastro");

    if (msgCadastro) {

        msgCadastro.style.display = "none";

        if (erro) {
            msgCadastro.style.display = "block";
            autoSumir(msgCadastro)
        }

        if (erro === "email_existente") {
            msgCadastro.innerText = "Esse email já está cadastrado !";
            msgCadastro.classList.add("mensagem-erro");
        }

        if (erro === "email_invalido") {
            msgCadastro.innerText = "Digite um email válido !";
            msgCadastro.classList.add("mensagem-erro");
        }

        if (erro === "erro_email") {
            msgCadastro.innerText = "Conta criada, mas erro ao enviar email !";
            msgCadastro.classList.add("mensagem-erro");
        }

        if (erro === "erro_geral") {
            msgCadastro.innerText = "Erro ao cadastrar. Tente novamente !";
            msgCadastro.classList.add("mensagem-erro");
        }
    }

    if (window.location.search) {
        window.history.replaceState({}, document.title, window.location.pathname);
    }

});

/* =========================
AUTO-SUMIR MENSAGENS
========================= */

function autoSumir(elemento) {
    if (!elemento) return;

    setTimeout(() => {
        elemento.style.transition = "opacity 0.5s ease";
        elemento.style.opacity = "0";

        setTimeout(() => {
            elemento.style.display = "none";
            elemento.style.opacity = "1"; // reset
        }, 500);

    }, 4000); // tempo (4 segundos)

}

/* =========================
REENVIAR VERIFICAÇÃO
========================= */

document.addEventListener("DOMContentLoaded", () => {

    const toggle = document.querySelector(".reenviar-toggle");
    const box = document.querySelector(".reenviar-box");
    const textoFixo = document.querySelector(".texto-fixo");

    if (toggle && box && textoFixo) {

        toggle.addEventListener("click", () => {

            box.classList.toggle("ativo");

            if (box.classList.contains("ativo")) {

                // 🔥 esconde só o texto
                textoFixo.style.display = "none";

                // muda botão
                toggle.innerHTML = "Ocultar ▲";

            } else {

                // 🔥 mostra o texto novamente
                textoFixo.style.display = "inline";

                // volta botão
                toggle.innerHTML = "Reenviar";

            }
        });
    }
});

/* =========================
MOSTRAR / OCULTAR SENHA
========================= */

function mostrarSenha(elemento) {
    let input = elemento.parentElement.querySelector("input");

    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password";
        elemento.textContent = "👁";
    }
}

/* =========================
INICIALIZAÇÃO
========================= */

document.addEventListener("DOMContentLoaded", () => {

    iniciarGraficos()

    carregarTransacoes()

    const btnNova = document.getElementById("btnNovaTransacao")

    if (btnNova) {
        btnNova.addEventListener("click", () => {
            document.getElementById("modalTransacao").style.display = "flex"
        })
    }

})

/* =========================
CATEGORIAS
========================= */

const categorias = {
    trabalho: { nome: "Trabalho", cor: "#13e035" },
    moradia: { nome: "Moradia", cor: "#ff6b6b" },
    educacao: { nome: "Educação", cor: "#4dabf7" },
    investimento: { nome: "Investimento", cor: "#006811" },
    alimentacao: { nome: "Alimentação", cor: "#ffd43b" },
    transporte: { nome: "Transporte", cor: "#845ef7" },
    outros: { nome: "Outros", cor: "#868e96" }
}

/* =========================
GRÁFICOS
========================= */

let chart
let chartReceitas

function iniciarGraficos() {

    const ctx = document.getElementById("grafico")
    const ctxReceitas = document.getElementById("graficoReceitas")

    if (!ctx || !ctxReceitas) return

    chart = new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: Object.values(categorias).map(c => c.nome),
            datasets: [{
                data: [0, 0, 0, 0, 0, 0, 0],
                backgroundColor: Object.values(categorias).map(c => c.cor),
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            cutout: "65%",
            plugins: { legend: { display: false } }
        }
    })

    chartReceitas = new Chart(ctxReceitas, {
        type: "doughnut",
        data: {
            labels: Object.values(categorias).map(c => c.nome),
            datasets: [{
                data: [0, 0, 0, 0, 0, 0, 0],
                backgroundColor: Object.values(categorias).map(c => c.cor),
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            cutout: "65%",
            plugins: { legend: { display: false } }
        }
    })

}

/* =========================
ATUALIZAR DASHBOARD
========================= */

function atualizar() {

    let receitas = 0
    let despesas = 0

    const totaisCategoria = {
        trabalho: 0,
        moradia: 0,
        educacao: 0,
        investimento: 0,
        alimentacao: 0,
        transporte: 0,
        outros: 0
    }

    const receitasCategoria = { ...totaisCategoria }

    const lista = document.getElementById("lista")

    if (!lista) return

    lista.innerHTML = ""

    transacoes.forEach(t => {

        let valor = Number(t.valor)

        if (t.tipo === "receita") {
            receitas += valor
            if (receitasCategoria[t.categoria] !== undefined)
                receitasCategoria[t.categoria] += valor
        } else {
            despesas += valor
            if (totaisCategoria[t.categoria] !== undefined)
                totaisCategoria[t.categoria] += valor
        }

        const div = document.createElement("div")
        div.className = "item"

        div.innerHTML = `

<span>${formatarData(t.data_criacao)}</span>

<span>${categorias[t.categoria]?.nome || t.categoria}</span>

<span>${t.descricao}</span>

<span class="${t.tipo === "receita" ? "green" : "red"}">
${t.tipo === "receita" ? "Receita" : "Despesa"}
</span>

<span class="${t.tipo === "receita" ? "green" : "red"}">
R$ ${valor.toFixed(2)}
</span>

<span class="acoes">
<button onclick="editarTransacao(${t.id})" class="btn-editar">✏️</button>
<button onclick="abrirModalExcluir(${t.id})" class="btn-excluir">🗑</button>
</span>

`
        lista.appendChild(div)

    })

    let saldo = receitas - despesas

    document.getElementById("saldo").innerText = "R$ " + saldo.toFixed(2)
    document.getElementById("receitas").innerText = "R$ " + receitas.toFixed(2)
    document.getElementById("despesas").innerText = "R$ " + despesas.toFixed(2)

    if (chart) {

        chart.data.datasets[0].data = [
            totaisCategoria.trabalho,
            totaisCategoria.moradia,
            totaisCategoria.educacao,
            totaisCategoria.investimento,
            totaisCategoria.alimentacao,
            totaisCategoria.transporte,
            totaisCategoria.outros
        ]

        chart.update()

    }

    if (chartReceitas) {

        chartReceitas.data.datasets[0].data = [
            receitasCategoria.trabalho,
            receitasCategoria.moradia,
            receitasCategoria.educacao,
            receitasCategoria.investimento,
            receitasCategoria.alimentacao,
            receitasCategoria.transporte,
            receitasCategoria.outros
        ]

        chartReceitas.update()

    }

    if (despesas > receitas)
        document.getElementById("alerta").style.display = "block"
    else
        document.getElementById("alerta").style.display = "none"

}

/* =========================
CARREGAR TRANSAÇÕES
========================= */

function carregarTransacoes() {

    fetch("bd_connect/listar_transacoes.php")

        .then(res => res.json())

        .then(data => {

            transacoes = data.map(t => ({
                ...t,
                valor: Number(t.valor)
            }))

            atualizar()

        })

        .catch(() => {

            console.log("Erro ao carregar transações")

        })

}

/* =========================
FORMATAR DATA
========================= */

function formatarData(data) {

    const d = new Date(data)

    return d.toLocaleString("pt-BR", {
        day: "2-digit",
        month: "2-digit",
        year: "numeric",
    })

}

/* =========================
ADICIONAR / EDITAR
========================= */

function salvarTransacao() {

    let categoria = document.getElementById("categoria").value
    let desc = document.getElementById("desc").value
    let valor = document.getElementById("valor").value
    let tipo = document.getElementById("tipo").value
    let fixo = document.getElementById("fixo").value

    let url = ""
    let body = ""

    // 👉 EDITANDO
    if (indexEditando !== null) {

        url = "bd_connect/editar_transacao.php"

        body =
            "id=" + indexEditando +
            "&categoria=" + categoria +
            "&descricao=" + desc +
            "&valor=" + valor +
            "&tipo=" + tipo +
            "&fixo=" + fixo

    } else {

        // 👉 NOVA
        url = "bd_connect/salvar_transacoes.php"

        body =
            "categoria=" + categoria +
            "&descricao=" + desc +
            "&valor=" + valor +
            "&tipo=" + tipo +
            "&fixo=" + fixo
    }

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: body
    })
        .then(res => res.json())
        .then(data => {

            if (data.status === "ok") {

                fecharModal()
                carregarTransacoes()
                limparFormulario()

                indexEditando = null

            } else {
                alert("Erro ao salvar")
            }

        })

}

/* =========================
EDITAR TRANSAÇÃO
========================= */

function editarTransacao(id) {

    const t = transacoes.find(t => t.id == id)

    document.getElementById("categoria").value = t.categoria
    document.getElementById("desc").value = t.descricao
    document.getElementById("valor").value = t.valor
    document.getElementById("tipo").value = t.tipo
    document.getElementById("fixo").value = t.fixo

    indexEditando = id

    document.getElementById("modalTransacao").style.display = "flex"

    document.getElementById("btn-salvar").innerText = "Atualizar"
}

/* =========================
LIMPAR FORMULÁRIO
========================= */

function limparFormulario() {

    document.getElementById("categoria").value = "trabalho"
    document.getElementById("desc").value = ""
    document.getElementById("valor").value = ""
    document.getElementById("tipo").value = "receita"
    document.getElementById("fixo").value = "fixa"

    document.getElementById("btn-salvar").innerText = "Adicionar"

}

/* =========================
NOVA TRANSAÇÃO
========================= */

document.getElementById("btnNovaTransacao").addEventListener("click", () => {

    limparFormulario()
    indexEditando = null

    document.getElementById("modalTransacao").style.display = "flex"

})

/* =========================
MODAL EXCLUIR
========================= */

function abrirModalExcluir(id) {
    indexExcluir = id
    document.getElementById("modalExcluir").style.display = "flex"
}

function confirmarExcluir() {

    console.log("ID para excluir:", indexExcluir)

    if (indexExcluir !== null) {

        fetch("bd_connect/excluir_transacao.php", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: "id=" + indexExcluir
        })
            .then(res => res.json())
            .then(data => {
                console.log("Resposta:", data)

                if (data.status === "ok") {
                    carregarTransacoes()
                }
            })
    }

    fecharModalExcluir()
}

function fecharModalExcluir() {
    document.getElementById("modalExcluir").style.display = "none"
}

/* =========================
MODAL TRANSAÇÃO
========================= */

function fecharModal() {

    document.getElementById("modalTransacao").style.display = "none"

}

/* =========================
LOGOUT
========================= */

function abrirModalLogout() {

    document.getElementById("modalLogout").style.display = "flex"

}

function fecharModalLogout() {

    document.getElementById("modalLogout").style.display = "none"

}

function confirmarLogout() {

    window.location.href = "bd_connect/logout.php"

}

/* =========================
SIMULADOR CDI
========================= */

function simularCDI() {

    let valor = parseFloat(document.getElementById("invest").value)
    let meses = parseFloat(document.getElementById("meses").value)

    let cdi = 0.011

    let total = valor * Math.pow(1 + cdi, meses)

    document.getElementById("cdiResultado").innerText =
        "Valor final: R$ " + total.toFixed(2)

}

/* =========================
SIMULADOR JUROS
========================= */

function simularJuros() {

    let divida = parseFloat(document.getElementById("divida").value)
    let juros = parseFloat(document.getElementById("juros").value) / 100
    let meses = parseFloat(document.getElementById("tempo").value)

    let total = divida * Math.pow(1 + juros, meses)

    document.getElementById("jurosResultado").innerText =
        "Total da dívida: R$ " + total.toFixed(2)

}

/* =========================
BACK TO TOP
========================= */

document.querySelector('.container').scrollTo({
    top: 0,
    behavior: 'smooth'
});
