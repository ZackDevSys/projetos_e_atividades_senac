<?php

session_start();
include "conexao.php";

if (!isset($_SESSION['usuario_id'])) {
    echo json_encode(["status" => "erro"]);
    exit();
}

$usuario_id = $_SESSION['usuario_id'];

$categoria = $_POST['categoria'];
$descricao = $_POST['descricao'];
$valor = $_POST['valor'];
$tipo = $_POST['tipo'];
$fixo = $_POST['fixo'];

$sql = "INSERT INTO transacoes 
(usuario_id, categoria, descricao, tipo, valor, fixa)
VALUES (?,?,?,?,?,?)";

$stmt = $conn->prepare($sql);
$stmt->bind_param("isssds", $usuario_id, $categoria, $descricao, $tipo, $valor, $fixo);
$stmt->execute();

echo json_encode(["status" => "ok"]);
