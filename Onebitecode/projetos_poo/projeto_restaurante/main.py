from class_cliente import Cliente
print('_________________________________________________\n')
print('     Seja bem vindo ao Restaurante Morramed')
print('_________________________________________________\n')


def cadastrar_cliente():
    tentativas = 0
    tentativas_cadastro = 3
    while tentativas < tentativas_cadastro:
        try:   
            print("Informe os seus dados:")
            nome_cliente = input("Nome:").strip().capitalize()
            print(nome_cliente)
            if not nome_cliente.replace(" ","").isalpha() or len(nome_cliente) < 3:
                tentativas +=1
                raise ValueError(f"Informe um nome válido com apenas caracteres do tipo e a cima de 2 caracteres\nTentativas:{tentativas} de {tentativas_cadastro}")
                break
            
            idade_cliente = input("Idade:")
            if not idade_cliente.isdigit() or len(idade_cliente) <=0:
                tentativas +=1
                raise ValueError(f"Informe uma idade válida\nTentativas:{tentativas} de {tentativas_cadastro}")
                break
            idade_cliente = int(idade_cliente)
            cpf_cliente = input("CPF:").strip()
            if not cpf_cliente.isdigit() or  len(cpf_cliente) < 11:
                tentativas +=1
                raise ValueError(f"Informe um CPF válido\nTentativas:{tentativas} de {tentativas_cadastro}")
                break
            cpf_cliente = f'{cpf_cliente[0:3]}.{cpf_cliente[3:6]}.{cpf_cliente[6:9]}-{cpf_cliente[9:11]}'
            
            bairro_cliente = input("Bairro:").strip().capitalize()
            if not bairro_cliente.isalpha():
                tentativas +=1
                raise ValueError(f"Informe um Bairro válido\nTentativas:{tentativas} de {tentativas_cadastro}")
                break
            rua_cliente = input("Rua:").strip().capitalize()
            if not rua_cliente.replace(" ","").isalpha():
                tentativas +=1
                raise ValueError(f"Informe uma rua válida\nTentativas:{tentativas} de {tentativas_cadastro}")
                break
            
            numero_endereco = input("Número:")
            if not numero_endereco.isdigit() or len(numero_endereco) <0:
                tentativas +=1
                raise ValueError(f"Informe uma número válido\nTentativas:{tentativas} de {tentativas_cadastro}")
                break
            numero_endereco = int(numero_endereco)
            
        except ValueError as erro:
            print(erro)
    if tentativas == tentativas_cadastro:
        print("Total de tentativas atingido.\nSaindo do programa ....")
    else:
        cliente_cadastrado = Cliente(nome_cliente,idade_cliente,cpf_cliente,bairro_cliente,rua_cliente,numero_endereco)    
        return cliente_cadastrado   
cadastrar_cliente()

