from flask import Flask, render_template, request
import json
import time

from dados.evento import Evento
from algoritmo_genetico.genetico import executar_algoritmo_genetico


app = Flask(__name__)


@app.route("/")
def inicio():
    evento = Evento(
        convidados=[
            "Ana",
            "João",
            "Carlos",
            "Maria",
            "Pedro",
            "Julia"
        ],
        quantidade_mesas=3,
        capacidade_mesa=2,
        preferencias=[
            (0, 1),
            (2, 3),
            (4, 5)
        ],
        conflitos=[]
    )

    inicio = time.perf_counter()

    melhor, fitness, historico = executar_algoritmo_genetico(
        evento,
        tamanho_populacao=50,
        numero_geracoes=50
    )

    fim = time.perf_counter()

    tempo_execucao = fim - inicio

    return render_template(
        "inicio.html",
        melhor=melhor,
        fitness=fitness,
        geracoes=len(historico),
        convidados=evento.convidados,
        quantidade_mesas=evento.quantidade_mesas,
        tempo_execucao=tempo_execucao
    )


@app.route("/organizar", methods=["POST"])
def organizar():
    convidados = request.form.getlist("convidados")
    quantidade_mesas = int(request.form["quantidade_mesas"])
    capacidade_mesa = int(request.form["capacidade_mesa"])
    relacionamentos = request.form.getlist("relacionamentos")

    print("Relacionamentos recebidos:", relacionamentos)

    preferencias = []
    conflitos = []

    for relacionamento in relacionamentos:

        dados = json.loads(relacionamento)

        pessoa1 = dados["pessoa1"]
        pessoa2 = dados["pessoa2"]
        tipo = dados["tipo"]

        if tipo == "preferencia":
            preferencias.append((pessoa1, pessoa2))

        elif tipo == "conflito":
            conflitos.append((pessoa1, pessoa2))


    evento = Evento(
        convidados=convidados,
        quantidade_mesas=quantidade_mesas,
        capacidade_mesa=capacidade_mesa,
        preferencias=preferencias,
        conflitos=conflitos
    )

    inicio = time.perf_counter()

    melhor, fitness, historico = executar_algoritmo_genetico(
        evento,
        tamanho_populacao=50,
        numero_geracoes=50
    )

    fim = time.perf_counter()

    tempo_execucao = fim - inicio

    preferencias_atendidas = 0
    conflitos_encontrados = 0

    for pessoa_a, pessoa_b in preferencias:
        if melhor.genes[pessoa_a] == melhor.genes[pessoa_b]:
            preferencias_atendidas += 1

    for pessoa_a, pessoa_b in conflitos:
        if melhor.genes[pessoa_a] == melhor.genes[pessoa_b]:
            conflitos_encontrados += 1

    return render_template(
        "inicio.html",
        melhor=melhor,
        fitness=fitness,
        geracoes=len(historico),
        convidados=convidados,
        quantidade_mesas=quantidade_mesas,
        preferencias_atendidas=preferencias_atendidas,
        conflitos_encontrados=conflitos_encontrados,
        tempo_execucao=tempo_execucao
    )


if __name__ == "__main__":
    app.run(debug=True)