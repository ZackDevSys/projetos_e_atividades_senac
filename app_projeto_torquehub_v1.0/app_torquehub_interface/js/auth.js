/* =========================================================
   TORQUEHUB
   AUTENTICAÇÃO
========================================================= */


/* =========================================================
   ELEMENTOS DA TELA
========================================================= */

const formularioLogin =
    document.getElementById("formulario-login");

const mensagemLogin =
    document.getElementById("mensagem-login");


/* =========================================================
   LOGIN
========================================================= */

if (formularioLogin) {

    formularioLogin.addEventListener(
        "submit",
        async function (event) {

            event.preventDefault();


            /* =================================================
               CAMPOS
            ================================================= */

            const email =
                document
                    .getElementById("email")
                    .value
                    .trim();


            const senha =
                document
                    .getElementById("senha")
                    .value;


            /* =================================================
               LIMPAR MENSAGEM
            ================================================= */

            mensagemLogin.textContent = "";

            mensagemLogin.className =
                "mensagem-login";


            /* =================================================
               VALIDAÇÃO
            ================================================= */

            if (!email || !senha) {

                mostrarMensagem(
                    "Preencha o e-mail e a senha.",
                    "erro"
                );

                return;

            }


            /* =================================================
               DESABILITAR BOTÃO
            ================================================= */

            const botao =
                formularioLogin.querySelector(
                    ".botao-login"
                );


            if (botao) {

                botao.disabled = true;

                botao.textContent =
                    "Entrando...";

            }


            try {

                /* =============================================
                   ENVIAR LOGIN PARA A API
                ============================================= */

                const resultado =
                    await apiPost(
                        "/login",
                        {
                            email: email,
                            senha: senha
                        }
                    );


                console.log(
                    "Resposta do login:",
                    resultado
                );


                /* =============================================
                   VERIFICAR USUÁRIO RETORNADO
                ============================================= */

                const usuario =
                    resultado?.dados;


                if (!usuario) {

                    throw new Error(
                        "A API não retornou os dados do usuário."
                    );

                }


                /* =============================================
                   SALVAR USUÁRIO
                ============================================= */

                localStorage.setItem(
                    "torquehub_usuario",
                    JSON.stringify(usuario)
                );


                /* =============================================
                   MENSAGEM DE SUCESSO
                ============================================= */

                mostrarMensagem(
                    "Login realizado com sucesso!",
                    "sucesso"
                );


                /* =============================================
                   REDIRECIONAR
                ============================================= */

                setTimeout(
                    function () {

                        window.location.href =
                            "dashboard.html";

                    },
                    500
                );


            } catch (erro) {

                console.error(
                    "Erro no login:",
                    erro
                );


                mostrarMensagem(
                    erro.message ||
                    "Não foi possível realizar o login.",
                    "erro"
                );


                /* =============================================
                   REATIVAR BOTÃO
                ============================================= */

                if (botao) {

                    botao.disabled = false;

                    botao.textContent =
                        "Entrar no sistema";

                }

            }

        }
    );

}


/* =========================================================
   EXIBIR MENSAGEM
========================================================= */

function mostrarMensagem(
    mensagem,
    tipo
) {

    if (!mensagemLogin) {
        return;
    }


    mensagemLogin.textContent =
        mensagem;


    mensagemLogin.className =
        "mensagem-login";


    mensagemLogin.classList.add(
        tipo
    );

}