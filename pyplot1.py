import pandas as pd
import matplotlib.pyplot as plt

dados = [[1186, 1751], [21328,2528], [947, 18432], [29, 280]]
linhas = ['Estadual', 'Privada', 'Municipal', 'Federal']
colunas =['Número de Alunos', 'Número de Professores']
df = pd.DataFrame(dados, index=linhas, columns=colunas)
df['Tipo de Escola'] = linhas

df.plot.barh(x="Tipo de Escola", y="Número de Alunos", orientation='horizontal', color='purple')
plt.title("Número de Alunos por Tipo de Escola")
plt.xlabel("Número de Alunos")
plt.ylabel("Tipo de Escola")
plt.show()