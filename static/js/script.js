const botaoAdicionar = document.getElementById("adicionar-convidado");
const listaConvidados = document.getElementById("lista-convidados");

botaoAdicionar.addEventListener("click", function () {
    const novoCampo = document.createElement("input");

    novoCampo.type = "text";
    novoCampo.name = "convidados";
    novoCampo.placeholder = "Nome do convidado";
    novoCampo.required = true;

    listaConvidados.appendChild(novoCampo);
});