class Cardapio:
    dict_comida = {'0': 'Nenhuma Opção',
    "1":"Camarão - 50R$",
    "2":"Risoto de Queijos - 60R$",
    "3":"Batata frita c/Bacon - 25R$",
    "4":"Carbonara - 40R$",
    "5":"Hamburguer - 37R$"}
    
    dict_bebida = {
        '0': 'Nenhuma Opção',
        '1': 'Água - 5R$',
        '2': 'Refri - 7R$',
        '3': 'Suco - 10R$',
        '4': 'Whisky - 27R$'}
    

    @staticmethod
    def cardapio_comida():
        print("===== Cardápio Pratos =====")
        for chave,valor in Cardapio.dict_comida.items():
            print(chave,valor)
        print("====================================================")
        
    @staticmethod
    def cardapio_bebida():
        print("===== Cardápio Bebidas =====")
        for chave,valor in Cardapio.dict_bebida.items():
            print(chave,valor,)
        print("====================================================")
    @staticmethod        
    def valores_comida(chave_comida):
        dict_comida_valores = {'0': 0,
        "1":50,
        "2":60,
        "3":25,
        "4":40,
        "5":37}
        chave_comida_str = str(chave_comida)
        valor_comida = dict_comida_valores.get(chave_comida_str,0)
        return valor_comida
    @staticmethod
    def valores_bebida(chave_bebida):    
        dict_comida_bebida = {'0': 0,
        "1":5,
        "2":7,
        "3":10,
        "4":27}
        chave_bebida_str = str(chave_bebida)
        valor_bebida = dict_comida_bebida.get(chave_bebida_str,0)
        return valor_bebida
# valor_comida = Cardapio.valores_bebida(7)  # Chama o método e retorna 60
# print(valor_comida)  