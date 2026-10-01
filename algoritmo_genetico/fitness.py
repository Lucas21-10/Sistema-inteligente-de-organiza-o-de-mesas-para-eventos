RECOMPENSA_PREFERENCIA = 10
PENALIDADE_CONFLITO = 20
PENALIDADE_EXCESSO = 50

def mesma_mesa(individuo, pessoa_a, pessoa_b):
    return individuo.genes[pessoa_a] == individuo.genes[pessoa_b]

def calcular_fitness(individuo, evento):
    pontuacao = 0

    # preferências
    for pessoa_a, pessoa_b in evento.preferencias:
        if mesma_mesa(individuo, pessoa_a, pessoa_b):
            pontuacao += RECOMPENSA_PREFERENCIA

    # conflitos
    for pessoa_a, pessoa_b in evento.conflitos:
        if mesma_mesa(individuo, pessoa_a, pessoa_b):
            pontuacao -= PENALIDADE_CONFLITO

    # excesso
    ocupacao_mesas = [0] * evento.quantidade_mesas

    for mesa in individuo.genes:
        ocupacao_mesas[mesa - 1] += 1

    for ocupacao in ocupacao_mesas:
        if ocupacao > evento.capacidade_mesa:
            excesso = ocupacao - evento.capacidade_mesa
            pontuacao -= excesso * PENALIDADE_EXCESSO

    return pontuacao



