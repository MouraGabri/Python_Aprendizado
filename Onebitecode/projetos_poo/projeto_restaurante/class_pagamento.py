from class_cliente import Cliente
class Pagamento:
    
    def __init__(self,cliente,valor_total_pedido):
        self.cliente = cliente # Armazenando a instancia de cliente
        self.valor_total_pedido = valor_total_pedido
    
    def depositar_saldo(self,novo_deposito_cliente):
        tentativas_cadastro = 3
        tentativas = 0
        while tentativas < tentativas_cadastro:
            try:
                if novo_deposito_cliente <=0:
                    novo_deposito_cliente = float(input('Não é possível depositar esse valor\nInforme um valor para deposito R$:').strip())
                    
                    if novo_deposito_cliente <=0:
                        tentativas +=1
                        print(f'Tentativa: {tentativas} de {tentativas_cadastro}')
                    continue
                
                self.cliente.saldo_conta += novo_deposito_cliente
                print(f'Deposito Efetuado com Sucesso. Saldo Atual: {self.cliente.saldo_conta:.2f} R$')
                break            
            except ValueError as erro:
                print(erro)
    
    def emitir_nota_fiscal(self,valor_total):
        print('==========Emitindo Nosta Fiscal==========')
        print(f'Nome:{self.cliente.nome}')
        print(f'CPF:{self.cliente.cpf}')
        print(f'Bairro:{self.cliente.bairro}')
        print(f'rua:{self.cliente.rua}')
        print(f'Valor Total da compra:{valor_total}')        
        
                    


