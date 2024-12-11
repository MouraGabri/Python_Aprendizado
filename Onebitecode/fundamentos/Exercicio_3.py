"""Faça um programa para escrever a contagem regressiva do lançamento de um 
foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”."""



contador = 10
print("---Contagem regressiva do foguete---")
while (contador >= 0):
    print(contador)
    contador -=1
print("beep") 


"""Faça um programa que calcule a tabuada de um número, com valores iniciais e 
finais informados pelo usuário""" 

numero_1 = int(input("Informe o número 1:"))
inicio = int(input("começa em que número:"))
fim = int(input("termina em que número:"))

while inicio <= fim:
    print(f'A tabuada do {numero_1} x {inicio} é {numero_1 * inicio}')
    inicio +=1
