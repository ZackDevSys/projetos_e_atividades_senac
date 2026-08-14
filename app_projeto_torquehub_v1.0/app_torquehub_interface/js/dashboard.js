const usuarioSalvo =
    localStorage.getItem("torquehub_usuario");

if (!usuarioSalvo) {

    window.location.href = "login.html";

} else {

    const usuario = JSON.parse(usuarioSalvo);

    const saudacao =
        document.getElementById("saudacao");


    if (saudacao) {

        saudacao.textContent =
            `Bem-vindo, ${usuario.nome}!`;
    }

    const botaoSair =
        document.getElementById("botao-sair");


    if (botaoSair) {

        botaoSair.addEventListener(
            "click",
            function () {

                localStorage.removeItem(
                    "torquehub_usuario"
                );

                window.location.href =
                    "login.html";

            }
        );

    }

}