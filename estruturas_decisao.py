# ## If e else
# print("1-Estudar\n2-Filme\n3-ler")
# oq_fazer_hoje_denoite = int(input("Escolhe 1 opção:"))

# if oq_fazer_hoje_denoite == 1:
#     print("Continue Gabriel")

# elif oq_fazer_hoje_denoite == 2:
#     print("Hoje não é dia")

# elif oq_fazer_hoje_denoite == 3:
#     print("ler".upper())   
# else: print("Volta a estudar")



# numero_1 = int(input("Informe um número:"))

# if numero_1 % 2 == 0:
#     print("Par")
# else:
#     print("Impar")
    
# nota = int(input("Informe a nota do aluno:"))

# if nota >= 9:
#  print("Recebe ss".upper()) 

# elif nota >= 7 and  nota < 9:
#  print("recebe ms")
 
# elif nota >= 5  and nota < 7:
#  print("recebe mm")

# else:
#  print("recebe mi")   

# "Faça um Programa que peça dois números e imprima o maior deles."
# num_1 = input("Número 1:")
# num_2 = input("Número 2:")
# if num_1 > num_2:
#     print(f"Número {num_1} maior")
# else:
#     print(f"Número {num_2} maior")    

# "Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo."
# num_1 = int(input("Número 1:"))
# if(num_1 >= 0):
#     print("Valor positivo")
# else:
#     print("Valor negativo")    

# "Faça um Programa que verifique se uma letra digitada é F ou M "
# "Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."
# sexo = input("Digite M ou F:")
# sexo = sexo.upper()
# if sexo == "M":
#     print("Masculino")
# elif sexo == "F":
#     print("Feminino")
# else:
#     print("Sexo Invalido")        
   

# ano = int(input("Informe o ano:"))
# if (ano % 4 == 0 and ano % 100 != 0)  or  (ano % 400 == 0):
#     print("ano bissexto")
# else:
#     print("não é bissexto")

# numero = int(input("Informe um número"))

# if( numero > 0):
#     print("Numero positivo")
# elif(numero < 0 ):
#     print("Numero negativo")

# else:
#     print("Zero")



print("---------Bem vindo ao Posto Cruz!-------- \n") 
print("           Promoções do dia:                  \n")
print("                ÁLCOOL                      ")
print("1- Até 20 litros, desconto de 3% por litro\n2- Acima de 20 litros, desconto de 5% por litro\n Valor do litro: R$ 1,90\n")

print("                GASOLINA                      ")
print("1- Até 20 litros, desconto de 4% por litro\n2- Acima de 20 litros, desconto de 6% por litro\n Valor do litro: R$ 2,50\n")

print("       Combustível: (A - ÁLCOOL) (G - GASOLINA)")
tipo_combust = input("Informe o Combustível:").upper()
qtd_litros   = float(input("Informe a quantidade de litros:"))


if(tipo_combust == "A" and qtd_litros > 0 and qtd_litros !=0 and qtd_litros <= 20):
        calc_sem_desconto = float(qtd_litros * (1.90))
        calc_desconto = float(calc_sem_desconto * (0.03))
        valor_para_pagar = calc_sem_desconto - calc_desconto
        print(f"Valor para pagar: R$ {valor_para_pagar}")


elif(tipo_combust == "A"  and qtd_litros > 0 and qtd_litros !=0 and qtd_litros > 20):
    calc_sem_desconto = qtd_litros * 1.90
    calc_desconto = calc_sem_desconto * (0.05)
    valor_para_pagar = calc_sem_desconto - calc_desconto 
    print(f"Valor para pagar: R$ {valor_para_pagar}")


elif(tipo_combust == "G" and qtd_litros > 0  and qtd_litros !=0 and qtd_litros <= 20):
        calc_sem_desconto = qtd_litros * 2.50
        calc_desconto = calc_sem_desconto * (0.04)
        valor_para_pagar = calc_sem_desconto - calc_desconto
        print(f"Valor para pagar: R$ {valor_para_pagar}")

elif(tipo_combust == "G"  and qtd_litros > 0  and qtd_litros !=0 and  qtd_litros > 20):
        calc_sem_desconto = qtd_litros * 2.50
        calc_desconto = calc_sem_desconto * (0.06)
        valor_para_pagar = calc_sem_desconto - calc_desconto
        print(f"Valor para pagar: R$ {valor_para_pagar}")
else:
     print("Não é possível abastecer com 0 ou litros negativos litros")
