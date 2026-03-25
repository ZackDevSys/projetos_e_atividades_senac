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

        $mail->Subject = "🚀 Confirme sua conta no FinUp";

        // 🔐 Segurança
        $nome = htmlspecialchars($nome);
        $link = htmlspecialchars($link);

        $mail->Body = "

<!DOCTYPE html>
<html>
<body style='margin:0; padding:0; background:#0B0F1A; font-family:Arial;'>

<div style='max-width:600px; margin:auto; padding:30px;'>

    <div style='background:#111827; border-radius:15px; padding:30px; text-align:center; color:#fff;'>

        <!-- LOGO -->
        <h1 style='margin-bottom:10px;'>
            <span style='color:#0F7BCA;'>Fin</span><span style='color:#F9860E;'>Up</span>
        </h1>

        <!-- TITULO -->
        <h2 style='margin-top:0;'>Confirme seu email 🚀</h2>

        <!-- TEXTO -->
        <p style='color:#cfd6e6; font-size:15px;'>
            Olá <strong>$nome</strong>,<br><br>
            Falta só um passo para começar sua evolução financeira.
        </p>

        <!-- BOTÃO -->
        <div style='margin:30px 0;'>

            <a href='$link' target='_blank'
            style='
                background: linear-gradient(135deg, #FF6A00, #F9860E);
                padding: 14px 28px;
                color: white;
                text-decoration: none;
                border-radius: 50px;
                font-weight: bold;
                display: inline-block;
                box-shadow: 0 10px 25px rgba(255,106,0,0.4);
            '>
                Confirmar Conta
            </a>

        </div>

        <!-- TEXTO FINAL -->
        <p style='font-size:13px; color:#aaa;'>
            Se você não criou essa conta, pode ignorar este email.
        </p>

    </div>

</div>

</body>
</html>

";

        // versão para email sem HTML
        $mail->AltBody = "Olá $nome, confirme sua conta: $link";

        $mail->send();

        return true;
    } catch (Exception $e) {

        return false;
    }
}
