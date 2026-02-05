<?php
session_start();

$perfil = $_POST['perfil'] ?? '';
$senha  = $_POST['senha'] ?? '';

// Senha exemplo (depois vem do banco)
$senhaPadrao = '123';

/* ❌ Nenhum perfil selecionado */
if ($perfil === '' || $perfil === '0') {
    header('Location: ../index.php?erro=perfil');
    exit;
}

/* ❌ Senha inválida */
if ($senha !== $senhaPadrao) {
    header('Location: ../index.php?erro=1');
    exit;
}

/* ✅ Login OK */
$_SESSION['perfil'] = $perfil;

/* 🔁 Redirecionamento por perfil */
switch ($perfil) {
    case 'admin':
        header('Location: ../admin.php');
        break;

    case 'estoquista':
        header('Location: ../estoque.php');
        break;

    case 'vendedor':
        header('Location: ../vendas.php');
        break;

    default:
        header('Location: ../index.php');
}
exit;
