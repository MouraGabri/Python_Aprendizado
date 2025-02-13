gamesList = ["Fifa", "God of War", "Red Dead 2", "Uncharted"]

# 1 - Iterando valores de uma lista 
# for i in gamesList:
#     print(i)

# 2 - Quando a condição for atendida, o loop será encerrado
# for i in gamesList:
#     if i == 'Red Dead 2':
#         break
#     print(i)

# 3 - Quando a condição for atendida, o loop vai para próxima interação
    # for i in gamesList:
    #     if i == 'Red Dead 2':
    #          continue
    #     print(i)
  
# 4 - Avaliação do Jogo
gameName = input("Nome do jogo:")
gameRating = int(input("Digite quantas avaliações deseja fazer no jogo:"))

soma = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo:"))
    soma = soma + note
print(f"A média de avaliação do jogo {gameName} é {soma/gameRating:.2f}")    
    
    