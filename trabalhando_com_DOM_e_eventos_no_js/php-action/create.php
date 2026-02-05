<?php

//................CONEXÃO................

include_once 'db_connect.php';

$nome = $_POST['nome_produto'];
$categoria = $_POST['categoria'];
$preco = $_POST['preco'];
$quantidade = $_POST['quantidade'];

$sql = "INSERT INTO estoque (nome_produto, categoria, preco, quantidade)
        VALUES ('$nome', '$categoria', '$preco', '$quantidade')";

if (mysqli_query($connect, $sql)) {
    // ✅ REDIRECIONA PARA A PÁGINA DE PRODUTOS
    header('Location: ../estoque.php?msg=sucesso_cadastro');
    exit();
} else {
    header('Location: ../estoque.php?msg=erro');
    exit();
}
