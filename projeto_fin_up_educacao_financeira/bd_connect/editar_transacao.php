<?php
session_start();
header("Content-Type: application/json");

$conn = new mysqli("localhost", "root", "", "finup");

if ($conn->connect_error) {
    echo json_encode(["status" => "erro"]);
    exit();
}

if (!isset($_SESSION['usuario_id'])) {
    echo json_encode(["status" => "erro"]);
    exit();
}

$id = $_POST['id'];
$categoria = $_POST['categoria'];
$descricao = $_POST['descricao'];
$valor = $_POST['valor'];
$tipo = $_POST['tipo'];
$fixa = $_POST['fixo'];
$usuario_id = $_SESSION['usuario_id'];

$sql = "UPDATE transacoes 
        SET categoria=?, descricao=?, valor=?, tipo=?, fixa=? 
        WHERE id=? AND usuario_id=?";

$stmt = $conn->prepare($sql);
$stmt->bind_param("ssdssii", $categoria, $descricao, $valor, $tipo, $fixa, $id, $usuario_id);

if ($stmt->execute()) {
    echo json_encode(["status" => "ok"]);
} else {
    echo json_encode(["status" => "erro"]);
}

$stmt->close();
$conn->close();
