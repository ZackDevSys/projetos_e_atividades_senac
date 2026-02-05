<?php

//................CONEXÃO................

require_once 'db_connect.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {

    $idcodigo   = mysqli_real_escape_string($connect, $_POST['idcodigo']);
    $nome       = mysqli_real_escape_string($connect, $_POST['nome_produto']);
    $categoria  = mysqli_real_escape_string($connect, $_POST['categoria']);
    $preco      = mysqli_real_escape_string($connect, $_POST['preco']);
    $quantidade = mysqli_real_escape_string($connect, $_POST['quantidade']);

    $sql = "UPDATE estoque SET 
                nome_produto = '$nome',
                categoria = '$categoria',
                preco = '$preco',
                quantidade = '$quantidade'
            WHERE idcodigo = '$idcodigo'";

    if (mysqli_query($connect, $sql)) {
        header('Location: ../estoque.php?msg=sucesso_edicao');
        exit;
    } else {
        header('Location: ../estoque.php?msg=erro');
        exit;
    }
}
