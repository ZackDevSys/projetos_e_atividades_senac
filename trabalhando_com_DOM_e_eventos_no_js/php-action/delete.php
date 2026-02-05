<?php

require_once 'db_connect.php';

if (isset($_GET['id'])) {

    $id = mysqli_real_escape_string($connect, $_GET['id']);

    $sql = "DELETE FROM estoque WHERE idcodigo = '$id'";

    if (mysqli_query($connect, $sql)) {
        header('Location: ../estoque.php?msg=sucesso_exclusao');
        exit;
    } else {
        header('Location: ../estoque.php?msg=erro');
        exit;
    }
}