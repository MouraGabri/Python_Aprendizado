game_Fifa = {
    "name": "Fifa 23",
    "yearLaunch": 2022,
    "gamePrice": 90.50,
    "classification": 8.5,
    "genre": ['esporte', "familia"]
}

# 1 - Recuperar um elemento do dicionário.
print(game_Fifa.get('name'))

# 2 - Buscar apenas as chaves do dicionário
print(game_Fifa.keys())

# 3 - Buscar apenas os valores do dicionário
print(game_Fifa.values())

# 4 - Buscar itens do dicionário com chave e valor
print(game_Fifa.items()) # Acaba retornando em uma tupla

# 5 - Adicionar itens no dicionário
game_Fifa["players"] = 2
print(game_Fifa)

# 6 - Atualizar itens no dicionário
game_Fifa.update({"players":4}) # Mudando para 4 ao invés de 2

# 7 - Remover iten no dicionário
game_Fifa.pop("players") # Removendo a chave

