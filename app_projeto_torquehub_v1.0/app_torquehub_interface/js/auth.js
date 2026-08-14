const formularioLogin = document.getElementById("formulario-login");
const mensagemLogin = document.getElementById("mensagem-login");

if (formularioLogin) {

    formularioLogin.addEventListener("submit", async function(event) {

        event.preventDefault();

        const email = document.getElementById("email").value.trim();
        const senha = document.getElementById("senha").value;

        mensagemLogin.textContent = "";
        mensagemLogin.className = "";

        if (!email || !senha) {

            mensagemLogin.textContent =
                "Preencha o email e a senha.";

            mensagemLogin.classList.add("erro");

            return;
        }

        try {

            const resultado = await fazerRequisicao("/login", {

                method: "POST",

                body: JSON.stringify({
                    email: email,
                    senha: senha
                })

            });

            const usuario = resultado.dados;

            /*
             * Guarda os dados do usuário
             * para utilizarmos no Dashboard.
             */
            localStorage.setItem(
                "torquehub_usuario",
                JSON.stringify(usuario)
            );

            mensagemLogin.textContent =
                "Login realizado com sucesso!";

            mensagemLogin.classList.add("sucesso");

            setTimeout(() => {

                window.location.href = "dashboard.html";

            }, 500);

        } catch (erro) {

            mensagemLogin.textContent = erro.message;

            mensagemLogin.classList.add("erro");
        }

    });

}