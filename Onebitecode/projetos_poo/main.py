from class_cliente import Cliente
from class_conta_bancaria import Conta_Bancaria

def cadastrar_cliente():
    print("-------Seja bem vindo-------")
    print("     Informe os seus dados\n")
    tentativas_cadastro = 3
    tentativas = 0
    while tentativas < tentativas_cadastro: 
        try:
            nome_pessoa = input("Informe o seu nome:").strip().capitalize()
            if not nome_pessoa.isalpha():
                tentativas +=1
                print(f'Tentivas:{tentativas} de {tentativas_cadastro} Tentativas')
                raise ValueError("O nome deve conter apenas letras.\n")
                break
            idade_pessoa = int(input("Informe a sua idade:"))
            if idade_pessoa < 0:
                tentativas +=1
                print(f'Tentivas:{tentativas} de {tentativas_cadastro} Tentativas')
                raise ValueError("Idade não pode ser negativa\n")
                break
            email_pessoa = input("Informe o seu E-mail:")
            if "@" not in email_pessoa or "." not in email_pessoa:
                tentativas +=1
                print(f'Tentivas:{tentativas} de {tentativas_cadastro} Tentativas')
                raise ValueError('Precisa ter "@" e "." no endereço de e-mail\n')
                break
            break
        except ValueError as erro:
            print(f'Erro:{erro}')
    if tentativas == tentativas_cadastro:        
        print('-----Tentativas atingidas-----\n     Saindo do Programa')
        exit()
    else:
        pessoa = Cliente(nome_pessoa,idade_pessoa,email_pessoa)
        print(pessoa)
        return pessoa                

def operacao_de_saque():
    cliente_cadastrado = cadastrar_cliente()
    conta_bancaria_cliente = Conta_Bancaria(cliente_cadastrado)
    tentativas = 0
    tentativas_escolha = 3
    while tentativas < tentativas_escolha:
        escolha = int(input('Escolha uma das Opções:\n[1] - Depositar Dinheiro\n[2] - Sacar Dinheiro\n[3] - Sair\nEscolha:'))
        if escolha == 1:
            valor_deposito = float(input('Informe o valor para deposito:'))
            conta_bancaria_cliente.depositar_dinheiro(valor_deposito)    
        elif escolha == 2:
            if conta_bancaria_cliente.saldo == 0:
                print('Você não possui nenhum saldo. Deposite primeiro')
                valor_deposito = float(input('Informe o valor para deposito:'))
                conta_bancaria_cliente.depositar_dinheiro(valor_deposito)
            valor_saque = float(input('Informe o valor para sacar:'))
            conta_bancaria_cliente.sacar_dinheiro(valor_saque)
        elif escolha == 3:
            exit()
        else:
            print('Escolha uma opção valida:')
            tentativas += 1
            print(f'Tentativa: {tentativas} de {tentativas_escolha}')
    if tentativas == tentativas_escolha:        
        print('-----Tentativas atingidas-----\n     Saindo do Programa')
        exit()
operacao_de_saque()




