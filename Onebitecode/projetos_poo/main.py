from class_cliente import Cliente
from class_conta_bancaria import Conta_Bancaria


def cadastrar_cliente():
    print("-------Seja bem vindo-------")
    print("     Informe os seus dados\n")
     
    try:
        nome = input("Informe o seu nome:").strip()
        if nome.isalpha():
            print('possui apenas string')
        else:
            raise ValueError("O nome deve conter apenas letras.")

        idade = int(input("Informe a sua idade:"))
        if idade < 0:
                raise ValueError("Idade não pode ser negativa")
            
        email = input("Informe o seu E-mail:")
        if "@" not in email or "." not in email:
                raise ValueError('Precisa ter "@" e "." no endereço de e-mail')        
    except ValueError as erro:
        print(f'Erro:{erro}')      
cadastrar_cliente()    
    