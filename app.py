from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask

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

    melhor, fitness, historico = executar_algoritmo_genetico(
        evento,
        tamanho_populacao=50,
        numero_geracoes=50
    )

    return render_template(
    "inicio.html",
    melhor=melhor,
    fitness=fitness,
    geracoes=len(historico)
)


if __name__ == "__main__":
    app.run(debug=True)