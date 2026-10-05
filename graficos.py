import matplotlib.pyplot as plt
import os


# Cria a pasta onde os gráficos serão salvos
os.makedirs("graficos", exist_ok=True)


# ==============================
# GRÁFICO 1 - FITNESS POR MUTAÇÃO
# ==============================

mutacoes = [5, 10, 20]
fitness = [20, 30, 30]

plt.figure(figsize=(8, 5))

plt.bar(mutacoes, fitness)

plt.title("Fitness por Taxa de Mutação")
plt.xlabel("Taxa de Mutação (%)")
plt.ylabel("Fitness")

plt.xticks(mutacoes)

plt.tight_layout()

plt.savefig("graficos/fitness_por_mutacao.png", dpi=300)

plt.close()


# ==============================
# GRÁFICO 2 - TEMPO POR MUTAÇÃO
# ==============================

tempos = [0.0135, 0.0169, 0.0621]

plt.figure(figsize=(8, 5))

plt.bar(mutacoes, tempos)

plt.title("Tempo de Execução por Taxa de Mutação")
plt.xlabel("Taxa de Mutação (%)")
plt.ylabel("Tempo (segundos)")

plt.xticks(mutacoes)

plt.tight_layout()

plt.savefig("graficos/tempo_por_mutacao.png", dpi=300)

plt.close()


# ==============================
# GRÁFICO 3 - COMPARAÇÃO DOS CENÁRIOS
# ==============================

cenarios = ["Cenário 1", "Cenário 2"]
quantidade_convidados = [20, 40]
tempos_cenarios = [0.0148, 0.0221]

plt.figure(figsize=(8, 5))

plt.bar(cenarios, tempos_cenarios)

plt.title("Tempo de Execução por Cenário")
plt.xlabel("Cenário")
plt.ylabel("Tempo (segundos)")

plt.tight_layout()

plt.savefig("graficos/comparacao_cenarios.png", dpi=300)

plt.close()


print("Gráficos gerados com sucesso!")
print("Arquivos salvos na pasta 'graficos'.")