<?php

session_start();
include "conexao.php";

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    $email = trim($_POST['email'] ?? '');
    $senha = $_POST['senha'] ?? '';
    
    $stmt = $conn->prepare("SELECT * FROM usuarios WHERE email = ?");
    $stmt->bind_param("s", $email);
    $stmt->execute();
    $resultado = $stmt->get_result();

    if ($resultado->num_rows > 0) {

        $usuario = $resultado->fetch_assoc();

        if (password_verify($senha, $usuario['senha'])) {

            if ($usuario['verificado'] == 0) {

                header("Location: ../login.php?erro=nao_verificado&email=$email");
                exit();
            }

            // 🔐 segurança extra
            session_regenerate_id(true);

            $_SESSION['usuario_id'] = $usuario['id'];
            $_SESSION['usuario_nome'] = $usuario['usuario'];

            header("Location: ../dashboard.php");
            exit();
        } else {

            header("Location: ../login.php?erro=senha_incorreta");
            exit();
        }
    } else {

        header("Location: ../login.php?erro=email_nao_existe");
        exit();
    }
}

$conn->close();
