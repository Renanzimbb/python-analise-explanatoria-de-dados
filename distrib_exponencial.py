#Exponecial
from scipy.stats import expon
# definir a média lambda
lambda_ = 1/2

# calcular a probabilidade com scipy.stats
prob = expon.cdf(3, scale=1/lambda_)

# exibir a probabilidade
print(prob)