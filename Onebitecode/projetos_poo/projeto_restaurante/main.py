from class_cliente import Cliente
from class_cardapio import Cardapio
from class_pedido import Pedido
from class_pagamento import Pagamento
import time
print('_________________________________________________\n')
print('     Seja bem vindo ao Restaurante Morramed')
print('_________________________________________________\n')

def cadastrar_cliente():
    tentativas_cadastro = 3
    
    tentativas = 0  # Reinicia as tentativas para o próximo campo
    while tentativas < tentativas_cadastro:    
        try:    
            nome_cliente = input("Nome:").strip().capitalize()
            if not nome_cliente.replace(" ","").isalpha() or len(nome_cliente) < 3:
                tentativas += 1
                raise ValueError(f"Informe um nome válido com apenas caracteres do tipo e acima de 2 caracteres\nTentativas:{tentativas} de {tentativas_cadastro}")
            break   
        except ValueError as erro:
            print(erro)
    else:
        print("Total de tentativas atingido para o nome. Saindo do programa...")
        exit()  # Sai do programa se atingir o número máximo de tentativas

    # Repetir o mesmo processo para os outros campos
    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            idade_cliente = input("Idade:")
            if not idade_cliente.isdigit() or len(idade_cliente) <= 0:
                tentativas += 1
                raise ValueError(f"Informe uma idade válida\nTentativas:{tentativas} de {tentativas_cadastro}")
            idade_cliente = int(idade_cliente)
            break
        except ValueError as erro:
            print(erro)
    else:
        print("Total de tentativas atingido para a idade. Saindo do programa...")
        exit()

    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            cpf_cliente = input("CPF:").strip()
            if not cpf_cliente.isdigit() or len(cpf_cliente) < 11:
                tentativas += 1
                raise ValueError(f"Informe um CPF válido\nTentativas:{tentativas} de {tentativas_cadastro}")
            cpf_cliente = f'{cpf_cliente[0:3]}.{cpf_cliente[3:6]}.{cpf_cliente[6:9]}-{cpf_cliente[9:11]}'
            break
        except ValueError as erro:
            print(erro)
    else:
        print("Total de tentativas atingido para o CPF. Saindo do programa...")
        exit()

    # Continuar o mesmo fluxo para os outros campos
    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            bairro_cliente = input("Bairro:").strip().capitalize()
            if not bairro_cliente.isalpha():
                tentativas += 1
                raise ValueError(f"Informe um Bairro válido\nTentativas:{tentativas} de {tentativas_cadastro}")
            break
        except ValueError as erro:
            print(erro)
    else:
        print("Total de tentativas atingido para o bairro. Saindo do programa...")
        exit()

    tentativas = 0  
    while tentativas < tentativas_cadastro:    
        try:    
            rua_cliente = input("Rua:").strip().capitalize()
            if not rua_cliente.replace(" ","").isalpha():
                tentativas += 1
                raise ValueError(f"Informe uma rua válida\nTentativas:{tentativas} de {tentativas_cadastro}")
            break
        except ValueError as erro:
            print(erro)
    else:
        print("Total de tentativas atingido para a rua. Saindo do programa...")
        exit()

    tentativas = 0      
    while tentativas < tentativas_cadastro:    
        try:    
            numero_endereco = input("Número:")
            if not numero_endereco.isdigit() or len(numero_endereco) < 0:
                tentativas += 1
                raise ValueError(f"Informe um número válido\nTentativas:{tentativas} de {tentativas_cadastro}")
            numero_endereco = int(numero_endereco)
            break
        except ValueError as erro:
            print(erro)        
    else:
        print("Total de tentativas atingido para o número. Saindo do programa...")
        exit()

    tentativas = 0
    while tentativas < tentativas_cadastro:    
        try:    
            saldo_cliente = input('Saldo inicial da conta: R$').strip()
            if not saldo_cliente:
                tentativas += 1
                raise ValueError(f"Saldo não pode estar vazio!\nTentativas: {tentativas} de {tentativas_cadastro}")
            saldo_cliente = float(saldo_cliente)
            if saldo_cliente < 0:
                tentativas += 1
                raise ValueError(f"Saldo não pode ser negativo!\nTentativas: {tentativas} de {tentativas_cadastro}")
            break
        except ValueError as erro:
            print(erro)
    else:
        print("Total de tentativas atingido para o saldo. Saindo do programa...")
        exit()

    # Se o cadastro for bem sucedido, retorna o cliente
    cliente_cadastrado = Cliente(nome_cliente, idade_cliente, cpf_cliente, bairro_cliente, rua_cliente, numero_endereco, saldo_cliente)
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
    return opcao_comida,opcao_bebida



def fazer_pagamento(cliente_cadastrado,pedido_cliente):
    opcao_comida, opcao_bebida = pedido_cliente  # Desempacotamento correto

    if opcao_bebida == '0':
        valor_bebida = 0
    else:
        valor_bebida = Cardapio.valores_bebida(opcao_bebida)

    if opcao_comida == '0':
        valor_comida = 0
    else:
        valor_comida = Cardapio.valores_comida(opcao_comida)
                
    print(f"Valor do Prato escolhido:{valor_comida}")
    print(f"Valor da Bebida Escolhida:{valor_bebida}")
    valor_total = float(valor_comida) + float(valor_bebida)
    print(f'Total do Pedido: {valor_total:.2f}')
    print("Iniciando Processo de pagamento:")
    print(f'Saldo Atual:{cliente_cadastrado.saldo_conta}\n')

    novo_cliente = Pagamento(cliente_cadastrado,valor_total)

    if cliente_cadastrado.saldo_conta < valor_total:
        print('Você não possui saldo suficiente para pagar\Faça outro deposito.')
        deposito_cliente = float(input("Valor:"))
        novo_cliente.depositar_saldo(deposito_cliente)
    
    else:
        print('Relizando Pagamento....')
        time.sleep(2)
        saldo_cliente = cliente_cadastrado.saldo_conta - valor_total
        print("Pagamento Efetuado com Sucesso:")
        print(f"Saldo Atual:{saldo_cliente:.2f}")
        novo_cliente.emitir_nota_fiscal(valor_total)

cliente_cadastrado = cadastrar_cliente()

if cliente_cadastrado:
    pedido_cliente = escolher_pedido()
    fazer_pagamento(cliente_cadastrado,pedido_cliente)
else:
    print('Cliente Não cadastrado')    
    
        