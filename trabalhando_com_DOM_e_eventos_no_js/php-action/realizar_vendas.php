<?php
session_start();
include_once 'db_connect.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $codigo = intval($_POST['codigo_produto']);
    $qtdVenda = floatval($_POST['quantidade_venda']);

    $sqlProd = "SELECT * FROM estoque WHERE idcodigo = $codigo";
    $resProd = mysqli_query($connect, $sqlProd);
    $produto = mysqli_fetch_assoc($resProd);

    if (!$produto) {
        header("Location: ../vendas.php?msg_venda=Produto não encontrado!");
        exit;
    }

    if ($produto['quantidade'] < $qtdVenda) {
        header("Location: ../vendas.php?msg_venda=Estoque insuficiente!");
        exit;
    }

    $total = $qtdVenda * $produto['preco'];

    mysqli_query(
        $connect,
        "INSERT INTO vendas (codigo_produto, nome_produto, quantidade, preco_kg, total)
         VALUES ($codigo, '{$produto['nome_produto']}', $qtdVenda, {$produto['preco']}, $total)"
    );

    mysqli_query(
        $connect,
        "UPDATE estoque SET quantidade = quantidade - $qtdVenda WHERE idcodigo = $codigo"
    );

    header("Location: ../vendas.php?msg_venda=Venda registrada com sucesso!");
    exit;
}

