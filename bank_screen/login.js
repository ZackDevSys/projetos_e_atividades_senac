document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault(); // impede envio padrão do form

    const cliente = document.getElementById("cliente").value;
    const senha = document.getElementById("senha").value;

    // Seleciona ou cria a mensagem de erro
    let erro = document.getElementById("erro");
    if (!erro) {
        erro = document.createElement("p");
        erro.id = "erro";
        erro.style.color = "red";
        erro.style.textAlign = "center";
        erro.style.marginTop = "10px";
        document.getElementById("loginForm").appendChild(erro);
    }

    // Validação simulada
    if (cliente === "admin" && senha === "1234") {
        window.location.href = "contaBancaria.html";
    } else {
        erro.textContent = "Cliente ou senha inválidos";
    }
});
