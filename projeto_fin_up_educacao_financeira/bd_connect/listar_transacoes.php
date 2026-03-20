<?php

session_start();
include "conexao.php";

/* verificar se usuário está logado */

if (!isset($_SESSION['usuario_id'])) {
    echo json_encode([]);
    exit();
}

$usuario_id = $_SESSION['usuario_id'];

$sql = "SELECT * FROM transacoes WHERE usuario_id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $usuario_id);
$stmt->execute();

$resultado = $stmt->get_result();

$transacoes = [];

while ($row = $resultado->fetch_assoc()) {
    $transacoes[] = $row;
}

echo json_encode($transacoes);
