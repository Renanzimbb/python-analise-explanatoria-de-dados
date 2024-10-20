#Hypergeometrica
import scipy.stats as stats
# Criar uma distribuição hipergeométrica com M = 100, n = 20 e N = 10
distribuicao = stats.hypergeom(100, 20, 10)
# Calcular a probabilidade de obter exatamente 3 sucessos na amostra - probability mass function
probabilidade_3_sucessos = distribuicao.pmf(3)
distribuicao.pmf(3)
# Calcular a probabilidade de obter 3 ou menos sucessos na amostra
probabilidade_3_ou_menos_sucessos = distribuicao.cdf(3)
# Calcular a média e a variância da distribuição
media = distribuicao.mean()
variancia = distribuicao.var()
# Exibir resultados
print("Probabilidade de obter exatamente 3 sucessos na amostra: ", probabilidade_3_sucessos)
print("Probabilidade de obter 3 ou menos sucessos na amostra: ", probabilidade_3_ou_menos_sucessos)
print("Média: ", media)
print("Variância: ", variancia)