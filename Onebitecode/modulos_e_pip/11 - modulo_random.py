import random


# 1 - Selecionando valor aleatório de uma lista
list = [4,5,1,4,2,6,9,4]
print(random.choice(list))

# 2 - Gera um número aleatório em um intervalo de valores
r1 = random.randint(5,15)
print(r1)

# 3 - Seleciona carcetere aleatório de uma string
texto = "Curso Python"
r2 = random.choice(texto)
print(r2)

# 4 - Selecionar mais de um valor aleatório
print(random.sample(list,2))


import os
print(os.getcwd())