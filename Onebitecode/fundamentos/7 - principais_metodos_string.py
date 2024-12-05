gameName = "fifa 23"
gameDescription = """
Fifa é um jogo de futebol desenvolvido pela EA Sports,
 e que possibilita jogar localmente ou online
"""

# print(gameName.upper()) ## Retorna string em maiúsculo
# print(gameName.lower()) ## Retorna string em minúsculo
# print(gameName.capitalize()) ## Apenas primeira letra em maiusculo
# print(gameName.title()) ## Apenas primeira letra em maiusculo
# print(gameName.center(10,'-')) # Retorna a string centralizada com caractere de preenchimento
# print(gameName.find("a")) # Retorna a posição de um determinado caractere
# print(gameDescription.count("a")) # Conta caracteres
# print(gameDescription.replace("Fifa","Mario")) # Altere um elemento por outro
# print(gameDescription.split(' , ')) # Dividir a string em partes com base em um delimitador


# nova_palavra =  gameName[:2] + "$" + gameName[3:]
# print(nova_palavra)


# var_1 = gameName[0].lower()
# var2 = gameName[1:]
# var_3 = var2.replace("f","$")
# cont = var_1 + var_3
# print(cont)

string_1 = "abc"
string_2 = 'xyz'

print(string_2[0:2] + string_1[2], string_1[0:2] + string_2[2])
