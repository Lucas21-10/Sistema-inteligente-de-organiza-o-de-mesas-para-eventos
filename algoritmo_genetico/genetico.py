from .individuo import Individuo


def criar_populacao(tamanho_populacao, quantidade_convidados, quantidade_mesas):
    populacao = []

    for _ in range(tamanho_populacao):
        individuo = Individuo.aleatorio(
            quantidade_convidados,
            quantidade_mesas
        )

        populacao.append(individuo)

    return populacao

