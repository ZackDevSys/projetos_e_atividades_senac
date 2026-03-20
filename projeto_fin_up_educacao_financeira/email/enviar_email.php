<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require_once __DIR__ . '/../PHPMailer/src/PHPMailer.php';
require_once __DIR__ . '/../PHPMailer/src/SMTP.php';
require_once __DIR__ . '/../PHPMailer/src/Exception.php';

function enviarEmail($emailDestino, $nome, $link)
{
    $mail = new PHPMailer(true);

    try {

        $mail->isSMTP();

        $mail->Host = 'smtp.gmail.com';
        $mail->SMTPAuth = true;

        $mail->Username = EMAIL_USER;
        $mail->Password = EMAIL_PASS;

        $mail->SMTPSecure = 'tls';
        $mail->Port = 587;

        $mail->CharSet = 'UTF-8';

        $mail->setFrom('finup.educacao.financeira@gmail.com', 'FinUp');

        $mail->addAddress($emailDestino, $nome);

        $mail->isHTML(true);

        $mail->Subject = "Confirme seu cadastro no FinUp";

        // 🔐 Segurança
        $nome = htmlspecialchars($nome);
        $link = htmlspecialchars($link);

        $mail->Body = "

<h2>Bem-vindo ao FinUp</h2>

<p>Olá <b>$nome</b></p>

<p>Clique no botão abaixo para confirmar sua conta:</p>

<a href='$link'
    style='
background:#FF6A00;
padding:12px 25px;
color:white;
text-decoration:none;
border-radius:30px;
font-weight:bold;
'>Confirmar Conta</a>

<p>Se você não criou uma conta ignore este email.</p>

";

        // versão para email sem HTML
        $mail->AltBody = "Olá $nome, confirme sua conta: $link";

        $mail->send();

        return true;
    } catch (Exception $e) {

        return false;
    }
}
