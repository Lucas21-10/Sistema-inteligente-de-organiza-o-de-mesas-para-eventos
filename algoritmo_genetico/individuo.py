import random


class Individuo:
    def __init__(self, genes):
        self.genes = genes

    @classmethod
    def aleatorio(cls, quantidade_convidados, quantidade_mesas):
        genes = []

        for _ in range(quantidade_convidados):
            mesa = random.randint(1, quantidade_mesas)
            genes.append(mesa)

        return cls(genes)

