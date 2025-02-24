class Cardapio:
    
    @staticmethod
    def cardapio_comida():
        print("===== Cardápio Pratos =====")
        dict_comida = {"1":"Camarão - 50R$","2":"Risoto de Queijos - 60R$","3":"Batata frita c/Bacon - 25R$","4":"Carbonara - 40R$","5":"Hamburguer - 37R$"}
        for chave,valor in dict_comida.items():
            print(chave,valor)
        print("====================================================")
        
    @staticmethod
    def cardapio_bebida():
        print("===== Cardápio Bebidas =====")
        dict_comida = {"1":"Água - 5R$","2":"Refri - 7R$","3":"Suco - 10R$","4":"Whisky - 27R$","5":"Chá - 5R$"}
        for chave,valor in dict_comida.items():
            print(chave,valor,)
        print("====================================================")    


Cardapio.cardapio_comida()
Cardapio.cardapio_bebida()