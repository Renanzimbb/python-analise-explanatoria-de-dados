import pandas as pd
import matplotlib.pyplot as plt

dados = [[1186, 1751], [21328,2528], [947, 18432], [29, 280]]
linhas = ['Estadual', 'Privada', 'Municipal', 'Federal']
colunas =['Número de Alunos', 'Número de Professores']
df = pd.DataFrame(dados, index=linhas, columns=colunas)

#cores = ['red', 'green', 'blue','orange']
#dados_alunos = df['Número de Alunos']
#plt.pie(dados_alunos, labels=dados_alunos.index, autopct='%1.1f%%', colors= cores)
#plt.title("Distribuição do Número de Alunos por Tipo de Escola")
#plt.show()

fig, axs = plt.subplots(1, 2, figsize=(8, 4))

df.plot.pie(y="Número de Alunos", ax=axs[0], autopct="%1.1f%%", colors=["blue", "orange", "green", "red"], labels=None)
axs[0].set_title("Número de Alunos por Tipo de Escola")

df.plot.pie(y="Número de Professores", ax=axs[1], autopct="%1.1f%%", colors=["blue", "orange", "green", "red"], labels=None)
axs[1].set_title("Número de Professores por Tipo de Escola")
plt.tight_layout()
plt.show()