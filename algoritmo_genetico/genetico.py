import random
from .individuo import Individuo
from .fitness import calcular_fitness

def criar_populacao(tamanho_populacao, quantidade_convidados, quantidade_mesas):
    populacao = []

    for _ in range(tamanho_populacao):
        individuo = Individuo.aleatorio(
            quantidade_convidados,
            quantidade_mesas
        )

        populacao.append(individuo)

    return populacao

def avaliar_populacao(populacao, evento):
    resultados = []

    for individuo in populacao:
        fitness = calcular_fitness(individuo, evento)
        resultados.append((individuo, fitness))

    return resultados

def selecionar_por_torneio(resultados):
    competidores = random.sample(resultados, 2)

    vencedor = competidores[0]

    for competidor in competidores[1:]:
        if competidor[1] > vencedor[1]:
            vencedor = competidor

    return vencedor[0]


def crossover(pai_1, pai_2):
    ponto_corte = random.randint(1, len(pai_1.genes) - 1)

    genes_filho_1 = (
        pai_1.genes[:ponto_corte] +
        pai_2.genes[ponto_corte:]
    )

    genes_filho_2 = (
        pai_2.genes[:ponto_corte] +
        pai_1.genes[ponto_corte:]
    )

    filho_1 = Individuo(genes_filho_1)
    filho_2 = Individuo(genes_filho_2)

    return filho_1, filho_2

def mutacao(individuo, quantidade_mesas):
    posicao = random.randint(0, len(individuo.genes) - 1)
    mesa_atual = individuo.genes[posicao]

    mesas_disponiveis = [
        mesa for mesa in range(1, quantidade_mesas + 1)
        if mesa != mesa_atual
    ]

    nova_mesa = random.choice(mesas_disponiveis)

    individuo.genes[posicao] = nova_mesa


def executar_algoritmo_genetico(
    evento,
    tamanho_populacao=100,
    numero_geracoes=100,
    taxa_crossover=0.8,
    taxa_mutacao=0.1
):
    populacao = criar_populacao(
        tamanho_populacao,
        len(evento.convidados),
        evento.quantidade_mesas
    )

    melhor_individuo = None
    melhor_fitness = float("-inf")
    historico_fitness = []

    for geracao in range(numero_geracoes):
        resultados = avaliar_populacao(populacao, evento)

        resultados.sort(key=lambda resultado: resultado[1], reverse=True)

        if resultados[0][1] > melhor_fitness:
            melhor_individuo = resultados[0][0]
            melhor_fitness = resultados[0][1]

        historico_fitness.append(melhor_fitness)

        melhor_da_geracao = resultados[0][0]

        nova_populacao = [
            Individuo(melhor_da_geracao.genes.copy())
        ]

        while len(nova_populacao) < tamanho_populacao:
            pai_1 = selecionar_por_torneio(resultados)
            pai_2 = selecionar_por_torneio(resultados)

            if random.random() < taxa_crossover:
                filho_1, filho_2 = crossover(pai_1, pai_2)
            else:
                filho_1 = Individuo(pai_1.genes.copy())
                filho_2 = Individuo(pai_2.genes.copy())

            if random.random() < taxa_mutacao:
                mutacao(filho_1, evento.quantidade_mesas)

            if random.random() < taxa_mutacao:
                mutacao(filho_2, evento.quantidade_mesas)

            nova_populacao.append(filho_1)

            if len(nova_populacao) < tamanho_populacao:
                nova_populacao.append(filho_2)

        populacao = nova_populacao

    return melhor_individuo, melhor_fitness, historico_fitness



