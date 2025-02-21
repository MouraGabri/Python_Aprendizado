"""Classe Cliente com nome, idade, email.
Classe ContaBancaria associada ao cliente.
Métodos para depósito e saque."""

class Conta_Bancaria:

    def __init__(self,cliente,saldo=0.0):
        self.cliente = cliente
        self.saldo = saldo
        
    
    def depositar_dinheiro(self,valor):
        tentativas = 0
        tentativas_deposito = 3
        while tentativas < tentativas_deposito:
            try:    
                if valor < 0 or valor == 0:
                    tentativas +=1
                    print(f'Tentivas:{tentativas} de {tentativas_deposito} Tentativas')
                    raise ValueError('Não é possível depositar valores negativos ou nenhum valor')
                    break
                else:
                    self.saldo += valor
                    print(f'Cliente:{self.cliente.nome}')
                    print(f'Valor depositado:{valor}R$\nSaldo atual:{self.saldo} R$')
                    break
            except ValueError as erro:
                print(f'Erro:{erro}')
            
    
    def sacar_dinheiro(self,valor_saque):
        tentativas = 0
        tentativas_deposito = 3
        print(f'Olá {self.cliente.nome}. Saldo Atual:{self.saldo}')
        while tentativas < tentativas_deposito:
            try:    
                if valor_saque < 0 or valor_saque == 0:
                    tentativas +=1
                    print(f'Tentivas:{tentativas} de {tentativas_deposito} Tentativas')
                    raise ValueError('Não é possível sacar valores negativos ou nenhum valor')
                    break
                elif self.saldo < valor_saque:
                    tentativas +=1
                    print(f'Tentivas:{tentativas} de {tentativas_deposito} Tentativas')
                    raise ValueError(f'Você não possui saldo para Sacar (Saldo Atual:{self.saldo})')
                    break
                else:
                    self.saldo -= valor_saque
                    print(f'Cliente:{self.cliente.nome}')
                    print(f'Valor do saque:{valor_saque} R$\nSaldo atual:{self.saldo}  R$')
                break
            except ValueError as erro:
                print(f'Erro:{erro}')
        