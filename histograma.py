import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
import scipy.stats as stats

# Carregando o conjunto de dados California Housing
data = fetch_california_housing()

# Transformando em um DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
# Gerando o histograma da variável ‘MedInc’
plt.hist(df['MedInc'], bins=10, width=0.8)
# adiciona título e rótulos dos eixos
plt.title("Histograma dos dados do California Housing")
plt.xlabel('Valor')
plt.ylabel('Frequência')
plt.show()

# Realizar o teste de assimetria
med_inc = data.data[:,0]
statistic, pvalue = stats.skewtest(med_inc)
print(f'Statistic: {statistic}')
print(f'P-value: {pvalue}')