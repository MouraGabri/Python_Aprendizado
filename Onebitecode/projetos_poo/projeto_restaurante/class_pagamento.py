from class_cliente import Cliente
class Pagamento:
    
    def __init__(self,cliente):
        self.cliente = cliente # Armazenando a instancia de cliente
    
    def depositar_saldo(self,novo_deposito_cliente):
        tentativas_cadastro = 3
        tentativas = 0
        while tentativas < tentativas_cadastro:
            try:
                if novo_deposito_cliente <=0:
                    deposito_cliente = input('Não é possível depositar esse valor\nInforme um valor para deposito R$:').strip()
                    deposito_cliente = float(deposito_cliente) 
                    if deposito_cliente > 0:
                        deposito_cliente = float(deposito_cliente) 
                        saldo_atualizado = self.cliente.saldo_conta + deposito_cliente
                        print(f'Deposito Efetuado com Sucesso. Saldo Atual: {saldo_atualizado:.2f}')
                        break
                    else:
                        tentativas += 1
                        print(f'Não é possível depositar 0R$. Deposite outro valor.Tentativa:{tentativas} de {tentativas_cadastro}')
                if not novo_deposito_cliente <=0:
                    deposito_cliente = input('Informe um valor para deposito R$:').strip()
                    deposito_cliente = float(deposito_cliente) 
                    saldo_atualizado = self.cliente.saldo_conta + deposito_cliente
                    print(f'Deposito Efetuado com Sucesso. Saldo Atual: {saldo_atualizado:.2f}')
                    break            
            except ValueError as erro:
                print(erro)
                
cliente_2 = Cliente("João", 25, "12345678901", "Centro", "Rua A", "101", 100.0)
pagamento = Pagamento(cliente_2)
pagamento.depositar_saldo(0)
