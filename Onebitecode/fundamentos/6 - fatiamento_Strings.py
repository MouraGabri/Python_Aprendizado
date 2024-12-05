gameName = "Fifa 23"
gameDescription = """
Fifa é um jogo de futebol desenvolvido pela EA Sports
e que possibilita jogar localmente ou online
"""

#  string[inicio:fim] - indice começa em 0 | indice final -1

# Busque toda string a parit da primeira posição
#print(gameName[0:])

# Busque toda string até a última posição
#print(gameName[:7])

# Busque toda string da terceira até a última posição
#print(gameName[2:7])


"""
Funciona assim:
string[inicio:fim:passo] - índice começa na posição 0 | índice final -1
passo - determina o incremento. Por padrao esse número é o 1

Passo [ seria pegar o indice[0], pula o próximo e pega o outro]
que seria daí o [::2--> Passo, pega um e pula 1]
"""

# Busque toda a string de 2 em 2 caracteres
#print(gameName[::2])

# Pegue toda a string nos índices ímpares
print(gameName[1::2])

# Pegue toda a string nos índices pares
print(gameName[0::2])

#Inverter uma strig de trás para frente
print(gameName[::-1])