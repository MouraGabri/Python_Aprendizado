'''
Escreva uma função Python que receba uma string e 
conte o número de letras maiúsculas e minúsculas desta string.
'''

# def function(texto):
#     maiuscula = 0
#     minuscula = 0
#     for i in texto:
#         if i. isupper():
#             maiuscula += 1   
#         else:
#             minuscula +=1  
                      
#     print(f'maiscula {maiuscula}')   
#     print(f'minuscula {minuscula}')         
            
                    
# function('Gabriel')

"""
Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
"""


def function():
    numeros =  [10,5,3,4,6,1,0,50]  
    list_pares = [i for i in numeros if i % 2 ==0]
    print(f"Valores Pares {list_pares}")
    
    list_impares = [i for i in numeros if i % 2 !=0]
    print(f"Valores Impares {list_impares}")
                
function()        