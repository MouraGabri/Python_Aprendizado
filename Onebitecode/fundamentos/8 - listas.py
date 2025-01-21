lista_produtos = []


def cadastrando_produtos():
    quantidade_produtos = int(input('Informe a quantidade de produtos para comprar:').strip())
    produtos_comprados = 0
    while produtos_comprados < quantidade_produtos:
        produtos = input('Lista do supermercado:')
        lista_produtos.append(produtos)
        produtos_comprados +=1
    print('------------------------------------')

def remover_produtos():
    print(f'Produtos: {lista_produtos}', end= ' | ')
    print()
    
    while True:
        remover = input('Deseja remover produtos?')
        if remover == 'SIM':
            nome_produtos_remover = input('Informe o nome do produto para remover:').strip()
            lista_produtos.remove(nome_produtos_remover)
            print(f'Produtos Na lista: {lista_produtos}', end= ' | ')    
        else:
            print('Encerrando..')
            exit()
                            
cadastrando_produtos()
remover_produtos()
