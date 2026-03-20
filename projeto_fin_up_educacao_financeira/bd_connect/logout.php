<?php

session_start();

/* remove todas as sessões */
session_unset();
session_destroy();

/* redireciona para login */

header("Location: ../login.php");

exit();
