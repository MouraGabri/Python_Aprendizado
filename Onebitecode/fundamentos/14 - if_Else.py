name = input("Digite o nome do jogo\\n")
yearLaunch = int(input("Informe o ano de lançamento do jogo\\n"))
classification = float(input("Informe a nota de classificação do jogo\\n"))

if classification > 8.0 or yearLaunch > 2015:
    print("boa recomendação")
else:
    print("Péssima recomendação ")    