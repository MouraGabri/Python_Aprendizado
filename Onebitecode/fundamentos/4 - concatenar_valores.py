nome = input("Informe o nome do jogo:")
year_Lauch = int(input("Informe o ano do jogo:"))
gamePrice = float(input("Informe o valor do jogo:"))
planInclude = input("Esse jogo esta incluso no serviço mensal?")

print("----Informações do Jogo----")
print(f"Jogo: {nome}\n"
      f"Ano do Jogo: {year_Lauch}\n"
      f"Valor do jogo: {gamePrice}\n"
      f"Tem plano mensal: {planInclude}")