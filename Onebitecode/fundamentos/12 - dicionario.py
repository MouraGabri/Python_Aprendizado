produtos = {}

#Trabalhando com dicionários apenas
def cadastrar_produto():
    while True:
        opcao = input("Deseja Cadastrar algum produto?").upper()
        if opcao == 'SIM':
            produto = input("Informe o nome do produto:")
            valor = float(input("Informe o valor do produto:"))
            produtos[produto] = valor
        else:
            print('Saindo..')
            break    
    print(f'Produtos Cadastrados {produtos.items()}')

def remover_produto():
    while True:
        opcao = input("Deseja remover algum produto?").upper()
        if opcao == 'SIM':
            produto = input("Informe o nome do produto:")
            produtos.pop(produto)
        else:
            print('Saindo..')
            break    
    print(f'Produtos Cadastrados {produtos.items()}')
# cadastrar_produto()
# remover_produto()    

# Trabalhando com listas dentro de dicionários:
Carros = {}

#Trabalhando com dicionários apenas
def cadastrar_carro():
    while True:
        opcao = input("Deseja Cadastrar alguma marca?").upper()
        if opcao == 'SIM':
            marca = input("Informe o nome do marca:")
            carro = input("Informe os carros da marca separados por vírgula: ").strip()
            produtos.setdefault(marca, []).extend(carro.split(','))  # Inicializa e adiciona
        else:
            print('Saindo..')
            break    
    print(f'Produtos Cadastrados {produtos.items()}')
cadastrar_carro()

# Removendo apenas os valores dentro de uma lista que esta dentro de um dicionário.
def remover_carro():
    while True:
        marca = input("Informe o nome da marca para remover o carro: ")
        carro_a_remover = input("Informe o nome do carro a ser removido: ").strip()

        # Verifica se a marca existe no dicionário
        if marca in produtos:
            lista_carros = produtos[marca] # está acessando o valor associado à chave marca no dicionário produtos

            # Verifica se o carro está na lista da marca
            if carro_a_remover in lista_carros:
                # Encontra o índice do carro
                index = lista_carros.index(carro_a_remover)

                # Remove o carro usando o índice
                lista_carros.pop(index)
                print(f'O carro {carro_a_remover} foi removido da marca {marca}.')
            else:
                print(f'O carro {carro_a_remover} não foi encontrado na marca {marca}.')
        else:
            print(f'A marca {marca} não está cadastrada.')

        # Pergunta ao usuário se ele deseja remover outro carro
        continuar = input("Deseja remover outro carro? (SIM/NÃO): ").upper()
        if continuar != 'SIM':
            print('Saindo...')
            break

    print(f'Produtos atualizados: {produtos.items()}')