<?php

include "conexao.php";
include "config_email.php";
include "../email/enviar_email.php";

$email = $_POST['email'];

/* verificar usuário */

$stmt = $conn->prepare("SELECT id, usuario, verificado FROM usuarios WHERE email = ?");
$stmt->bind_param("s", $email);
$stmt->execute();

$resultado = $stmt->get_result();

if ($resultado->num_rows == 0) {
    header("Location: ../login.php?erro=email_nao_existe");
    exit();
    exit;
}

$usuario = $resultado->fetch_assoc();

if ($usuario['verificado'] == 1) {
    header("Location: ../login.php?sucesso=ja_verificado");
    exit();
    exit;
}

/* gerar novo token */

$token = bin2hex(random_bytes(32));

$update = $conn->prepare("UPDATE usuarios SET token = ? WHERE id = ?");
$update->bind_param("si", $token, $usuario['id']);
$update->execute();

/* criar link */

$link = "http://localhost/projeto_fin_up_educacao_financeira/bd_connect/verificar.php?token=$token";

/* enviar email */

if (enviarEmail($email, $usuario['usuario'], $link)) {
    header("Location: ../login.php?sucesso=email_reenviado");
    exit();
} else {
    header("Location: ../login.php?erro=erro_reenvio");
    exit();
}
