import scipy.stats as stats

# Definir a probabilidade de sucesso (p)
p = 0.3

# Definir o número de tentativas até o primeiro sucesso (k)
k = 5

# Calcular a probabilidade de X=k usando a função pmf da distribuição geométrica
probabilidade = stats.geom.pmf(k, p)

print(f"A probabilidade de precisar de exatamente {k} dardos é de {probabilidade:.4f}")



# Definir o número de tentativas até o primeiro sucesso (k)
#k = 1
# Calcular a probabilidade de X=k usando a função pmf da distribuição geométrica
#probabilidade = stats.geom.pmf(k, p)+stats.geom.pmf(k+1, p)