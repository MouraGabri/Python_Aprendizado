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

