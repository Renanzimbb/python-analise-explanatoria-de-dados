from scipy.stats import bernoulli

# Definindo a probabilidade de sucesso como 0.5
p = 0.5

# Criando a distribuição de Bernoulli
distribuicao = bernoulli(p)

# Calcular a média e a variância da distribuição
media = distribuicao.mean()
variancia = distribuicao.var()
print(media)
print(variancia)