class Viagem:

    def __init__(self,nome):
        self.nome = nome
        
    def __str__(self):
        return f'Seja bem vindo:{self.nome} -- Selecione uma das opções de viagem:'
    
    @staticmethod        
    def opcoes_viagem():
        print('Opções:\n1 - USA\n2 - California\n3 - Disney\n4 - Alaska')
        
    def escolha_viagem(self,escolha):
        dicionario_destino = {'1':'USA','2':'California','3':'Disney','4':'Alaska'}
        for chave,valor in dicionario_destino.items():    
            if chave == escolha:
                print(f'{self.nome} Obrigado por escolher o destino:{valor}')
                
         
cliente = Viagem('Gabriel')
print(cliente)
Viagem.opcoes_viagem()
cliente.escolha_viagem('1')
        
            
        