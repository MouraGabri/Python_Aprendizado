from class_cardapio import Cardapio
import re

class Pedido:
    
    @staticmethod
    def fazer_pedido_comida(chave_escolha_prato):
        # O método .get() usa uma tabela hash interna para acessar diretamente o valor associado à chave.
# A busca é feita de maneira eficiente, em tempo constante, independentemente do tamanho do dicionário.
# Isso significa que o Python não verifica chave por chave como em um loop (for), mas sim localiza diretamente o valor.

# O método .get() vai buscar a chave fornecida (chave_escolha_prato) no dicionário Cardapio.dict_comida. 
# Se a chave existir, ele retorna o valor associado a ela (ex: nome do prato e seu preço) e atribui esse valor à variável 'chave_escolha_prato'.
# Se a chave não for encontrada, o método retorna None (ou o valor padrão, se fornecido).
        chave_prato = Cardapio.dict_comida.get(chave_escolha_prato) # Busca diretamente no dicionário da outra classe
        if chave_prato:                
            palavra_formatada = re.findall(r'^[^\-]+(?=\s*-|\s*$)', chave_prato)
                
            if palavra_formatada:
                print(f"Prato escolhido: {palavra_formatada[0]}")      
            else:
                print(f"Prato escolhido: {palavra_formatada}")    
        if not chave_prato:
            print('Prato não encontrado')
    @staticmethod
    def fazer_pedido_bebida(chave_escolha_bebida):
            chave_escolha_bebida = Cardapio.dict_bebida.get(chave_escolha_bebida) # Busca diretamente no dicionário da outra classe
            if chave_escolha_bebida:                
                palavra_formatada = re.findall(r'^[^\-]+(?=\s*-|\s*$)', chave_escolha_bebida)
                    
                if palavra_formatada:
                    print(f"Bebida escolhido: {palavra_formatada[0]}")      
                else:
                    print(f"Bebida escolhido: {palavra_formatada}")    
            if not chave_escolha_bebida:
                print('Bebida não encontrado')

Pedido.fazer_pedido_bebida('4')

