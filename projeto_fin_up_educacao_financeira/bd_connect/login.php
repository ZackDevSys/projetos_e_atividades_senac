<?php

session_start();
include "conexao.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $email = $_POST['email'];
    $senha = $_POST['senha'];

    $sql = "SELECT * FROM usuarios WHERE email='$email'";
    $resultado = $conn->query($sql);

    if ($resultado->num_rows > 0) {

        $usuario = $resultado->fetch_assoc();

        if (password_verify($senha, $usuario['senha'])) {

            if ($usuario['verificado'] == 0) {

                echo "Confirme seu email antes de fazer login.<br><br>
                <form action='bd_connect/reenviar_verificacao.php' method='POST'>
                <input type='hidden' name='email' value='$email'>
                <button type='submit'>Reenviar email de verificação</button>
                </form>";
                exit();
            }

            $_SESSION['usuario_id'] = $usuario['id'];
            $_SESSION['usuario_nome'] = $usuario['usuario'];

            header("Location: ../dashboard.php");
            exit();
        } else {

            echo "Senha incorreta";
        }
    } else {

        echo "Usuário não encontrado";
    }
}

$conn->close();
