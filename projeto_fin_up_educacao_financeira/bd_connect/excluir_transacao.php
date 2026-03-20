<?php
session_start();
header("Content-Type: application/json");

// conexão com banco
$conn = new mysqli("localhost", "root", "", "finup");

if ($conn->connect_error) {
    echo json_encode([
        "status" => "erro",
        "mensagem" => "Erro na conexão"
    ]);
    exit();
}

// validar login
if (!isset($_SESSION['usuario_id'])) {
    echo json_encode([
        "status" => "erro",
        "mensagem" => "Usuário não autenticado"
    ]);
    exit();
}

// pegar dados
$id = $_POST['id'] ?? null;
$usuario_id = $_SESSION['usuario_id'];

if (!$id) {
    echo json_encode([
        "status" => "erro",
        "mensagem" => "ID não informado"
    ]);
    exit();
}

// segurança: só exclui se for do usuário logado
$sql = "DELETE FROM transacoes WHERE id = ? AND usuario_id = ?";

$stmt = $conn->prepare($sql);
$stmt->bind_param("ii", $id, $usuario_id);

if ($stmt->execute()) {

    echo json_encode([
        "status" => "ok"
    ]);
} else {

    echo json_encode([
        "status" => "erro",
        "mensagem" => "Erro ao excluir"
    ]);
}

$stmt->close();
$conn->close();
