from class_cliente import Cliente
from class_cardapio import Cardapio
from class_pedido import Pedido
import time
print('_________________________________________________\n')
print('     Seja bem vindo ao Restaurante Morramed')
print('_________________________________________________\n')

def cadastrar_cliente():
    tentativas_cadastro = 3
    
    tentativas = 0 # Reinicia as tentativas para o próximo campo
    while tentativas < tentativas_cadastro:    
        try:    
            nome_cliente = input("Nome:").strip().capitalize()
            if not nome_cliente.replace(" ","").isalpha() or len(nome_cliente) < 3:
                tentativas +=1
                raise ValueError(f"Informe um nome válido com apenas caracteres do tipo e a cima de 2 caracteres\nTentativas:{tentativas} de {tentativas_cadastro}")
            break   
        except ValueError as erro:
            print(erro)

    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            idade_cliente = input("Idade:")
            if not idade_cliente.isdigit() or len(idade_cliente) <=0:
                tentativas +=1
                raise ValueError(f"Informe uma idade válida\nTentativas:{tentativas} de {tentativas_cadastro}")
            idade_cliente = int(idade_cliente)
            break
        except ValueError as erro:
            print(erro)

    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            cpf_cliente = input("CPF:").strip()
            if not cpf_cliente.isdigit() or  len(cpf_cliente) < 11:
                tentativas +=1
                raise ValueError(f"Informe um CPF válido\nTentativas:{tentativas} de {tentativas_cadastro}")
            cpf_cliente = f'{cpf_cliente[0:3]}.{cpf_cliente[3:6]}.{cpf_cliente[6:9]}-{cpf_cliente[9:11]}'
            break
        except ValueError as erro:
            print(erro)

    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            bairro_cliente = input("Bairro:").strip().capitalize()
            if not bairro_cliente.isalpha():
                tentativas +=1
                raise ValueError(f"Informe um Bairro válido\nTentativas:{tentativas} de {tentativas_cadastro}")
            break
        except ValueError as erro:
            print(erro)

    tentativas = 0  
    while tentativas < tentativas_cadastro:    
        try:    
            rua_cliente = input("Rua:").strip().capitalize()
            if not rua_cliente.replace(" ","").isalpha():
                tentativas +=1
                raise ValueError(f"Informe uma rua válida\nTentativas:{tentativas} de {tentativas_cadastro}")
            break
        except ValueError as erro:
            print(erro)

    tentativas = 0      
    while tentativas < tentativas_cadastro:    
        try:    
            numero_endereco = input("Número:")
            if not numero_endereco.isdigit() or len(numero_endereco) <0:
                tentativas +=1
                raise ValueError(f"Informe uma número válido\nTentativas:{tentativas} de {tentativas_cadastro}")
            numero_endereco = int(numero_endereco)
            break
        except ValueError as erro:
            print(erro)        

    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            saldo_cliente = input('Saldo inicial da conta: R$').strip()
            # Verifica se o usuário não digitou nada (só apertou Enter)
            if not saldo_cliente:
                tentativas += 1
                raise ValueError(f"Saldo não pode estar vazio!\nTentativas: {tentativas} de {tentativas_cadastro}")
            saldo_cliente = float(saldo_cliente)
            if saldo_cliente < 0:
                tentativas += 1
                raise ValueError(f"Saldo não pode ser negativo!\nTentativas: {tentativas} de {tentativas_cadastro}")
            time.sleep(3)
            print('Processando Valor Depositado..')
            break
        except ValueError as erro:
            print(erro)

    if tentativas == tentativas_cadastro:
        print("Total de tentativas atingido.\nSaindo do programa ....")
    else:
        cliente_cadastrado = Cliente(nome_cliente,idade_cliente,cpf_cliente,bairro_cliente,rua_cliente,numero_endereco,saldo_cliente)
        print()  
        return cliente_cadastrado

def escolher_pedido():
    tentativas = 0
    tentativas_escolha = 3
    while tentativas < tentativas_escolha:
        try:
            escolha = input("Escolha uma das opções:\n[1] - Fazer Pedido\n[2] - Sair do Aplicativo\nOpção:")     
            if escolha == '1':
                print("Escolher os pratos")
                Cardapio.cardapio_comida()
                opcao_comida = input("Escolha um item do cardápio:")
                if opcao_comida in Cardapio.dict_comida:
                    Pedido.fazer_pedido_comida(opcao_comida)
                    break
                else:                    
                    tentativas +=1
                    Pedido.fazer_pedido_comida(opcao_comida)
                    raise ValueError(f"Tentativas:{tentativas} de {tentativas_escolha}")        

            elif escolha  == '2':
                print("Saindo do Sistema..")
                exit()
            else:
                tentativas +=1
                raise ValueError(f"Informe uma número válido\nTentativas:{tentativas} de {tentativas_escolha}")        
        except ValueError as erro:
            print(erro)
    while tentativas < tentativas_escolha:
        try:
            escolha_bebida = input("Deseja incluir bebida(Sim|Não):").strip().upper()
            if escolha_bebida == 'SIM':
                Cardapio.cardapio_bebida()
                opcao_bebida = input("Escolha um item do cardápio:")
                if opcao_bebida in Cardapio.dict_bebida and opcao_comida == '0' and opcao_bebida == '0':
                    print('Nenhum prato foi selecionado. Retornando ao menu..')
                    return escolher_pedido()
                else:
                    Pedido.fazer_pedido_bebida(opcao_bebida)
                    break
            elif escolha_bebida in ['NÃO','NAO'] and opcao_comida != '0':
                    opcao_bebida = '0'
                    Pedido.fazer_pedido_bebida(opcao_bebida)
                    break   
            elif escolha_bebida in ['NÃO','NAO'] and opcao_comida == '0':
                    # print('Nenhum prato foi selecionado. Retornando ao menu..')
                    return escolher_pedido()        
            else:
                print()
                tentativas +=1
                raise ValueError(f"Informe Apenas (Sim|Não)\nTentativas:{tentativas} de {tentativas_escolha}")        
        except ValueError as erro:
            print(erro)       
    if tentativas == tentativas_escolha:
        print("Total de tentativas atingido.\nSaindo do programa ....")
        exit()
    print('\n=====Pedidos Escolhidos=====:')
    Pedido.fazer_pedido_bebida(opcao_bebida)
    Pedido.fazer_pedido_comida(opcao_comida)
    print('===============================:')
    
if cadastrar_cliente():
    time.sleep(1)
    escolher_pedido()    