// CADASTRO DE CONVIDADOS

const listaConvidados = document.getElementById("lista-convidados");
const botaoAdicionarConvidado = document.getElementById("adicionar-convidado");

botaoAdicionarConvidado.addEventListener("click", function () {

    const novoCampo = document.createElement("input");

    novoCampo.type = "text";
    novoCampo.name = "convidados";
    novoCampo.placeholder = "Nome do convidado";
    novoCampo.required = true;

    listaConvidados.appendChild(novoCampo);

    atualizarPessoas();

    novoCampo.focus();
});



// PREFERÊNCIAS E CONFLITOS

const pessoa1 = document.getElementById("pessoa-1");
const pessoa2 = document.getElementById("pessoa-2");
const tipoRelacionamento = document.getElementById("tipo-relacionamento");

const botaoAdicionarRelacionamento =
    document.getElementById("adicionar-relacionamento");

const listaRelacionamentos =
    document.getElementById("lista-relacionamentos");


// Lista que armazenará os relacionamentos
const relacionamentos = [];



// ATUALIZA AS OPÇÕES DE PESSOAS

function atualizarPessoas() {

    const campos = document.querySelectorAll(
        'input[name="convidados"]'
    );

    const nomes = [];

    campos.forEach(function (campo) {

        const nome = campo.value.trim();

        if (nome !== "") {
            nomes.push(nome);
        }

    });


    atualizarSelect(pessoa1, nomes);
    atualizarSelect(pessoa2, nomes);
}



// ATUALIZA UM SELECT

function atualizarSelect(select, nomes) {

    const valorAtual = select.value;

    select.innerHTML = "";

    const opcaoInicial = document.createElement("option");

    opcaoInicial.value = "";
    opcaoInicial.textContent = "Pessoa";

    select.appendChild(opcaoInicial);


    nomes.forEach(function (nome, indice) {

        const opcao = document.createElement("option");

        opcao.value = indice;
        opcao.textContent = nome;

        select.appendChild(opcao);

    });


    if (valorAtual < nomes.length) {
        select.value = valorAtual;
    }
}



// ATUALIZA OS NOMES ENQUANTO O USUÁRIO DIGITA

listaConvidados.addEventListener("input", function () {

    atualizarPessoas();

});


// ADICIONAR RELACIONAMENTO

botaoAdicionarRelacionamento.addEventListener(
    "click",
    function () {

        const indicePessoa1 = pessoa1.value;
        const indicePessoa2 = pessoa2.value;

        const campos = document.querySelectorAll(
            'input[name="convidados"]'
        );

        const nomes = [];

        campos.forEach(function (campo) {

            const nome = campo.value.trim();

            if (nome !== "") {
                nomes.push(nome);
            }

        });


        // Verifica se as duas pessoas foram selecionadas
        if (indicePessoa1 === "" || indicePessoa2 === "") {

            alert("Selecione as duas pessoas.");

            return;
        }


        // Não permite a mesma pessoa
        if (indicePessoa1 === indicePessoa2) {

            alert("Uma pessoa não pode ter relacionamento com ela mesma.");

            return;
        }


        const nomePessoa1 = nomes[parseInt(indicePessoa1)];
        const nomePessoa2 = nomes[parseInt(indicePessoa2)];


        const relacionamento = {
            pessoa1: parseInt(indicePessoa1),
            pessoa2: parseInt(indicePessoa2),
            tipo: tipoRelacionamento.value
        };


        relacionamentos.push(relacionamento);


        // MOSTRAR NA TELA
        
        const item = document.createElement("div");

        item.classList.add("relacionamento-item");


        if (tipoRelacionamento.value === "preferencia") {

            item.innerHTML = `
                 ${nomePessoa1} + ${nomePessoa2}
            `;

        } else {

            item.innerHTML = `
                 ${nomePessoa1} × ${nomePessoa2}
            `;

        }


        listaRelacionamentos.appendChild(item);


        // Limpa as seleções
        pessoa1.value = "";
        pessoa2.value = "";

        

    }
);


// ENVIAR RELACIONAMENTOS PARA O FLASK

const formulario = document.querySelector("form");

formulario.addEventListener("submit", function () {

    relacionamentos.forEach(function (relacionamento) {

        const campo = document.createElement("input");

        campo.type = "hidden";
        campo.name = "relacionamentos";
        campo.value = JSON.stringify(relacionamento);

        formulario.appendChild(campo);

    });

});