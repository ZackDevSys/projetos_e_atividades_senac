<?php
include_once 'db_connect.php';

$data = [
    'produtos' => mysqli_fetch_row(mysqli_query($connect, "SELECT COUNT(*) FROM estoque"))[0],
    'estoque'  => mysqli_fetch_row(mysqli_query($connect, "SELECT SUM(quantidade) FROM estoque"))[0],
    'valor'    => mysqli_fetch_row(mysqli_query($connect, "SELECT SUM(preco * quantidade) FROM estoque"))[0],
    'vendas'   => mysqli_fetch_row(mysqli_query($connect, "SELECT SUM(total) FROM vendas WHERE DATE(data_venda)=CURDATE()"))[0],
];

echo json_encode($data);
