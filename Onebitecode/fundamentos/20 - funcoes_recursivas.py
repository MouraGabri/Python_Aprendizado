# Fatorial de um número:

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

number=  int(input('Digite um número para o fatorial:'))
factorial(number)   
print(f'O fatorial de {number} é {factorial(number)}')

# soma total de um número:
def sum(num):
    if num == 1:
        return 1 
    else:
        return num + factorial(num - 1)

number=  int(input('Digite um número para o fatorial:'))
factorial(number)   
print(f'O fatorial de {number} é {sum(number)}')