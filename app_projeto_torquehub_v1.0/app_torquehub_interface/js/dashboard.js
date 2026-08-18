const usuarioSalvo =
    localStorage.getItem("torquehub_usuario");


/*
 * Se não existir usuário salvo,
 * volta para o login.
 */
if (!usuarioSalvo) {

    window.location.href = "login.html";

} else {

    const usuario =
        JSON.parse(usuarioSalvo);


    /*
     * Saudação
     */

    const saudacao =
        document.getElementById("saudacao");


    if (saudacao) {

        saudacao.textContent =
            `Bem-vindo, ${usuario.nome}!`;
    }


    /*
     * Nome do usuário
     */

    const nomeUsuario =
        document.getElementById("nome-usuario");


    if (nomeUsuario) {

        nomeUsuario.textContent =
            usuario.nome;
    }


    /*
     * Perfil
     */

    const perfilUsuario =
        document.getElementById("perfil-usuario");


    if (perfilUsuario) {

        perfilUsuario.textContent =
            usuario.perfil;
    }


    /*
     * Avatar
     */

    const avatar =
        document.querySelector(".usuario-avatar");


    if (avatar && usuario.nome) {

        avatar.textContent =
            usuario.nome
                .charAt(0)
                .toUpperCase();
    }


    /*
     * Logout
     */

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