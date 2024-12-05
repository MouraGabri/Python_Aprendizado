distancia = int(input("Informe a quantidade de km:"))

if distancia <= 200:
    calc_1 = float(0.50 * distancia)
    print(f"Valor da passagem é {calc_1}$")
else:
    calc_2 = float(0.35 * distancia)
    print(f"Valor da passagem é {calc_2}$")


salario = float(input("Informe o seu salário:"))

if salario > 1250.00:
    aumento = salario * 0.10
    print(aumento)
    resultado = aumento + salario
    print(f"Seu salário é {resultado}$. Teve um aumento de {aumento}$")
else:
    aumento = salario * 0.15
    resultado = aumento + salario
    print(f"Seu salário é {resultado}$. Teve um aumento de {aumento}$")
        
