from scipy.stats import norm
# Definir média e desvio padrão
mu = 8
sigma = 2
# Definir o valor mínimo de retorno desejado (em R$)
retorno_minimo = 10
# Calcular a probabilidade com scipy.stats
probabilidade = 1 - norm.cdf(retorno_minimo, loc=mu, scale=sigma)
# Exibir a probabilidade
print(f"A probabilidade de ter um retorno superior a {retorno_minimo} reais é de {probabilidade:.2f}")


import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

# Parâmetros da distribuição normal
media = 170
desvio_padrao = 10

# Intervalo de alturas para o cálculo da densidade de probabilidade
alturas = np.linspace(media - 4 * desvio_padrao, media + 4 * desvio_padrao, 1000)

# Cálculo da densidade de probabilidade usando a função norm.pdf
densidade_probabilidade = norm.pdf(alturas, loc=media, scale=desvio_padrao)

# Criação do gráfico
plt.plot(alturas, densidade_probabilidade)
plt.xlabel('Altura (cm)')
plt.ylabel('Densidade de probabilidade')
plt.title('Distribuição normal para a altura de pessoas adultas')
plt.grid(True)
plt.show()