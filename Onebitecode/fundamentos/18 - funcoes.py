# Função para imprimir Hello Word
def welcome ():
    print('Hello Word')
 
welcome()
# Função para imprimir Hello Word

def sum():
   print(5 + 9)
   return 5 + 9   # Se eu quero imprimir só o return, preciso colocar com o print
sum()
print(sum()) 

# Cadastrar um jogo

def cadastrar_jogo():
    name = input("Digite o nome do jogo \\n")
    yearLaunch = int(input("Digite o ano de lançamento\\n"))
    gamePrice = float(input("Digite o preço do jogo\\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\\n"))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)
cadastrar_jogo()    
