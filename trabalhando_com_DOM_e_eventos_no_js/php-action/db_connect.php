<?php

//................CONEXÃO COM BANCO................

$servername = "sql201.infinityfree.com";
$username = "if0_41086649";
$password = "";
$db_name = "if0_41086649_estoque";

$connect = mysqli_connect($servername, $username, $password, $db_name);

if (mysqli_connect_error()):
    echo "Erro na conexão: " . mysqli_connect_error();
endif;
