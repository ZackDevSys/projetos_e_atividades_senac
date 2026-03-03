<?php
include_once 'db_connect.php';

$data = [
    'if0_41086649_estoque' => mysqli_fetch_row(mysqli_query($connect, "SELECT COUNT(*) FROM produtos"))[0],
    'produtos'  => mysqli_fetch_row(mysqli_query($connect, "SELECT SUM(quantidade) FROM produtos"))[0],
    'valor'    => mysqli_fetch_row(mysqli_query($connect, "SELECT SUM(preco * quantidade) FROM produtos"))[0],
    'vendas'   => mysqli_fetch_row(mysqli_query($connect, "SELECT SUM(total) FROM vendas WHERE DATE(data_venda)=CURDATE()"))[0],
];

echo json_encode($data);
