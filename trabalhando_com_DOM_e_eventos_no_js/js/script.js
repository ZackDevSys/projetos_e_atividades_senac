// Função para abrir o modal de exclusão
function abrirModal(id) {
    document.getElementById('modalExcluir').style.display = 'flex';
    document.getElementById('linkExcluir').href =
        'php-action/delete.php?id=' + id;
}

function fecharModal() {
    document.getElementById('modalExcluir').style.display = 'none';
}

function confirmarExclusao(id) {
    document.getElementById('linkExcluir').href =
        'php-action/delete.php?id=' + id;

    document.getElementById('modalExcluir').style.display = 'flex';
}

function fecharExcluir() {
    document.getElementById('modalExcluir').style.display = 'none';
}

// Desaparecer mensagem automaticamente
setTimeout(() => {
    const msg = document.querySelector('.msg');
    if (msg) {
        msg.style.opacity = '0';
        setTimeout(() => msg.remove(), 500);
    }
}, 5000); // desaparece após 5 segundos

// Funções para o modal de sair
function abrirModalSair() {
    document.getElementById('modalSair').style.display = 'flex';
}

function fecharModalSair() {
    document.getElementById('modalSair').style.display = 'none';
}

// Função para calcular o total da venda
const produto = document.getElementById('produto');
const quantidade = document.getElementById('quantidade');
const total = document.getElementById('total');
const totalHidden = document.getElementById('total_hidden');

if (produto && quantidade) {
    function calcularTotal() {
        const opt = produto.options[produto.selectedIndex];
        if (!opt) return;

        const preco = parseFloat(opt.dataset.preco || 0);
        const qtd = parseFloat(quantidade.value || 0);

        if (preco > 0 && qtd > 0) {
            const valor = preco * qtd;
            total.value = `R$ ${valor.toFixed(2).replace('.', ',')}`;
            totalHidden.value = valor.toFixed(2);
        } else {
            total.value = '';
            totalHidden.value = '';
        }
    }

    produto.addEventListener('change', calcularTotal);
    quantidade.addEventListener('input', calcularTotal);
}

// Desaparecer mensagem de erro de login automaticamente
const msg = document.getElementById('msgErro');
if (msg) {
    setTimeout(() => {
        msg.style.opacity = '0';
        msg.style.transition = 'opacity 0.5s';
        setTimeout(() => msg.remove(), 500);
    }, 3000);
}

// Função para atualizar o dashboard a cada 5 segundos
function atualizarDashboard() {
    fetch('php-action/dashboard_data.php')
        .then(res => res.json())
        .then(d => {
            document.querySelectorAll('.card strong')[0].innerText = d.produtos
            document.querySelectorAll('.card strong')[1].innerText = `${parseFloat(d.estoque).toFixed(2)} kg`
            document.querySelectorAll('.card strong')[2].innerText = `R$ ${parseFloat(d.valor).toFixed(2)}`
            document.querySelectorAll('.card strong')[3].innerText = `R$ ${parseFloat(d.vendas || 0).toFixed(2)}`
        })
}

setInterval(atualizarDashboard, 3000)
