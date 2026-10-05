import time

from dados.evento import Evento
from algoritmo_genetico.genetico import executar_algoritmo_genetico

# CENÁRIO 2
convidados = [f"Convidado {i + 1}" for i in range(40)]

evento = Evento(
    convidados=convidados,
    quantidade_mesas=5,
    capacidade_mesa=8,
    preferencias=[
        (0, 1),
        (2, 3),
        (4, 5),
        (6, 7),
        (8, 9),
        (10, 11),
        (12, 13),
        (14, 15),
        (16, 17),
        (18, 19)
    ],
    conflitos=[
        (20, 21),
        (22, 23),
        (24, 25),
        (26, 27),
        (28, 29)
    ]
)

inicio = time.perf_counter()

melhor, fitness, historico = executar_algoritmo_genetico(
    evento,
    tamanho_populacao=50,
    numero_geracoes=50
)

fim = time.perf_counter()

tempo = fim - inicio


print()
print("===== CENÁRIO 2 =====")
print("Convidados:", len(convidados))
print("Mesas:", evento.quantidade_mesas)
print("Capacidade por mesa:", evento.capacidade_mesa)
print("População:", 50)
print("Gerações:", 50)
print("Fitness:", fitness)
print("Tempo de execução:", round(tempo, 4), "segundos")
print("Melhor distribuição:", melhor.genes)




# TESTE DE TAXA DE MUTAÇÃO

convidados = [f"Convidado {i + 1}" for i in range(20)]

evento = Evento(
    convidados=convidados,
    quantidade_mesas=4,
    capacidade_mesa=5,
    preferencias=[
        (0, 1),
        (2, 3),
        (4, 5),
        (6, 7),
        (8, 9)
    ],
    conflitos=[
        (10, 11),
        (12, 13),
        (14, 15)
    ]
)

for taxa in [0.05, 0.10, 0.20]:

    inicio = time.perf_counter()

    melhor, fitness, historico = executar_algoritmo_genetico(
        evento,
        tamanho_populacao=50,
        numero_geracoes=50,
        taxa_mutacao=taxa
    )

    fim = time.perf_counter()

    tempo = fim - inicio

    print()
    print("===== TAXA DE MUTAÇÃO:", taxa * 100, "% =====")
    print("Fitness:", fitness)
    print("Tempo:", round(tempo, 4), "segundos")