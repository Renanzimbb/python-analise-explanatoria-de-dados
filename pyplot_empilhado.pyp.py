import pandas as pd
import matplotlib.pyplot as plt

dados = [[1186, 1751], [21328,2528], [947, 18432], [29, 280]]
linhas = ['Estadual', 'Privada', 'Municipal', 'Federal']
colunas =['Número de Alunos', 'Número de Professores']
df = pd.DataFrame(dados, index=linhas, columns=colunas)
df['Tipo de Escola'] = linhas

ax = df.plot.bar(stacked=True)
plt.title("Número de Alunos por Tipo de Escola")
plt.ylabel("Número de indivíduos")
plt.xlabel("Tipo de Escola")
plt.legend(loc='upper left')
plt.show()

# Gráfico de Dispersão
x = df["Número de Professores"]
y = df["Número de Alunos"]
plt.scatter(x, y)
plt.title("Relação entre Número de Professores e Número de Alunos")
plt.xlabel("Número de Professores")
plt.ylabel("Número de Alunos")
plt.show()