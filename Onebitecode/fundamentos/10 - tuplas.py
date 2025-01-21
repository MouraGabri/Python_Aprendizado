nome_carros = []

# Cadastrando uma tupla de Caracteristícas de carro em uma lista
def cadastrar_nomes_carro():
    while True:
        escolha = input("Deseja cadastrar um carro?").upper()
        if escolha == 'SIM':
            carro = input("Informe o nome do carro:").upper()
            modelo = input("Informe o modelo do carro:").upper()
            ano_carro = input("Informe o ano do carro:").upper()
            # Usando o método append da lista para adicionar tuplas na lista. Observa-se que coloquei () dentro dos () da lista,
            #Para armazenar como uma tupla
            nome_carros.append((carro,modelo,ano_carro))
        else:
            break    
    print(f'Carros cadastrados:{nome_carros}', end= ' | ')
print()
def remover_carro():       
    remover_veiculo = input("Deseja remover um carro?").upper()
    if remover_veiculo == 'SIM':
        carro_remover = input("Informe o nome do carro:").upper()
        modelo = input("Informe o modelo do carro:").upper()
        ano_carro = input("Informe o ano do carro:").upper()
        for tupla in nome_carros:
            if tupla[0] == carro_remover and tupla[1] == modelo and tupla[2] == ano_carro:
                print('esta na lista')
                #Precisei passar todas as variáveis para o formato de tupla, para poder excluir dentro da lista
                #Para excluir uma tupla dentro de uma lista, precisa passar ela no formato de tupla e por isso armazenei em uma variável do tipo
                #tupla
                tuplas_remover = (carro_remover,modelo,ano_carro)
                nome_carros.remove(tuplas_remover)
                print(f'Carros cadastrados:{nome_carros}', end= ' | ')
            else:
                print('Não possui cadastro')    
cadastrar_nomes_carro()
remover_carro()    