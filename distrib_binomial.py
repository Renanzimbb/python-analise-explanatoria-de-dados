#Binomial

import scipy.stats as stats

# Criar uma distribuição binomial com n = 20 e p = 0.2
distribuicao = stats.binom(20, 0.2)

# Calcular a probabilidade de obter exatamente 3 sucessos - probability mass function
probabilidade_8_sucessos = distribuicao.pmf(8)

# Calcular a probabilidade de obter 8 ou menos sucessos
probabilidade_8_ou_menos_sucessos = distribuicao.cdf(8)

# Calcular a média e a variância da distribuição
media = distribuicao.mean()
variancia = distribuicao.var()

# Exibir resultados
print("Probabilidade de obter exatamente 8 sucessos: ", probabilidade_8_sucessos)
print("Probabilidade de obter 8 ou menos sucessos: ", probabilidade_8_ou_menos_sucessos)
print("Média: ", media)
print("Variância: ", variancia)