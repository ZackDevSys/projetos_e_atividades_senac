<?php

include "conexao.php";
include "config_email.php";
include "../email/enviar_email.php";

$usuario = trim($_POST['usuario']);
$email = trim($_POST['email']);
$senha = $_POST['senha'];

if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    header("Location: ../cadastro.php?erro=email_invalido");
    exit();
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
    header("Location: ../cadastro.php?erro=email_existente");
    exit();
    exit;
}

/* inserir usuário */

$stmt = $conn->prepare("INSERT INTO usuarios (usuario,email,senha,token) VALUES (?, ?, ?, ?)");

$stmt->bind_param("ssss", $usuario, $email, $senhaHash, $token);

if ($stmt->execute()) {

    $link = "http://localhost/projeto_fin_up_educacao_financeira/bd_connect/verificar.php?token=$token";

    if (enviarEmail($email, $usuario, $link)) {
        header("Location: ../login.php?sucesso=verifique_email");
        exit();
    } else {
        header("Location: ../cadastro.php?erro=erro_email");
        exit();
    }
} else {
    header("Location: ../cadastro.php?erro=erro_geral");
    exit();
}
