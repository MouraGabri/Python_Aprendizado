import re
# # 1 - Índice inicial e final de palavras
# text = "Onebitecode: Gabriel Adao Michel Moura"
# # O r significa que estamos trabalhando com uma string bruta(row String)

# match =re.search(r'Gabriel Adao',text)
# print("indice inicial", match.start())
# print("indice Final", match.end())

# # 2 - Buscando o indice que possui o ponto
# site = 'https://onebitecode.com'
# match =re.search(r'\.',site)
# print(match)

# # 3 - Buscando uma lista de caracteres dentro de uma frase
# frase = "Gabriel Adao Michel Moura"
# padrao = "[G-a]"
# result = re.findall(padrao,frase)
# print(result)

# # 4 - Verificando o inicio de uma string
# rule = '^A'
# frase = ['ADAO','GBRIEL','AMOR']
# for i in frase:
#     if re.match(rule,i):
#         print(f'corresponde {i}')
#     else:
#         print(f' Não corresponde {i}')

# # 5 - Verificando o final de uma string
# rule_end = r'!$'
# frase = 'ADAO!'
# match = re.search(rule_end,frase)
# if match:
#     print(f'corresponde ')
# else:
#     print(f' Não corresponde ')
    
    
    # - Exercico Re
    

frase = 'Gabriel 194463'
padrao = r'\d'
resultado = re.search(padrao,frase)
print(resultado)


