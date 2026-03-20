<?php

include "conexao.php";
include "config_email.php";
include "../email/enviar_email.php";

$usuario = trim($_POST['usuario']);
$email = trim($_POST['email']);
$senha = $_POST['senha'];

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    echo "Email inválido.";
    exit;
}

$senhaHash = password_hash($senha, PASSWORD_DEFAULT);

$token = bin2hex(random_bytes(32));

/* verificar se email já existe */

$verifica = $conn->prepare("SELECT id FROM usuarios WHERE email = ?");
$verifica->bind_param("s", $email);
$verifica->execute();

$resultado = $verifica->get_result();

if ($resultado->num_rows > 0) {
    echo "Este email já está cadastrado.";
    exit;
}

/* inserir usuário */

$stmt = $conn->prepare("INSERT INTO usuarios (usuario,email,senha,token) VALUES (?, ?, ?, ?)");

$stmt->bind_param("ssss", $usuario, $email, $senhaHash, $token);

if ($stmt->execute()) {

    $link = "http://localhost/projeto_fin_up_educacao_financeira/bd_connect/verificar.php?token=$token";

    if (enviarEmail($email, $usuario, $link)) {
        echo "Cadastro realizado! Verifique seu email.";
    } else {
        echo "Usuário criado mas email não enviado.";
    }
} else {
    echo "Erro ao cadastrar.";
}
