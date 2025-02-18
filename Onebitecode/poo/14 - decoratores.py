from decorator import meu_decorate,upper_case,split_string
#Exemplo 1

@meu_decorate
def minha_funcao():
    print("Dentro da função")

minha_funcao()

# Exemplo 2
@upper_case
def text():
    return 'gabriel adão'

print(text())

# Exemplo 3
@split_string
@upper_case
def text_1():
    return 'aprendendo python e decoratores'

print(text_1())
 
