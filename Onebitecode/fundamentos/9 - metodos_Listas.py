games_list = ['Fifa','Mario', 'GTA', 'Red Dead 2', 'Zelda']

# 1 - tamanho da lista
print(len(games_list))

# 2 - Recuperar um item da lista pelo índice
print(games_list.index("Zelda"))

# 3 - Adicionar item ao final da lista
games_list.append("Fortnite")
print(games_list)

# 4 - Ordenar a lista
games_list.sort()
print(games_list)

# 5 - Copiar os itens de uma lista para outra
gameReset = games_list.copy() # Passando toda a lista
gameReset.remove("Fortnite")# Removendo o jogo da lista pois eu já zerei esse jogo
print(gameReset)

# 6 - Remove todos os itens da lista
gameReset.clear()
print(gameReset)