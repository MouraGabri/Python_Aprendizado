class Telefone: # Criando a Classe PAI
    
    def __init__(self,marca,modelo,preco):
        self._marca = marca
        self._modelo = modelo # Definindo como atributos protegidos
        self._preco = preco

    def __str__(self):
        return f'Marca:{self._marca} - Modelo:{self._modelo} - Preço:{self._preco}'
    
    @staticmethod
    def fazer_uma_ligacao(telefone):
        print(f'Ligando para {telefone}')
        
    def desconto(self):
        return self._preco * 0.10  
        
# Criando a Classe FILHA
#Classe filha herdando os atributos e métodos da classe pai(Telefone)
class Smarthphone(Telefone):
    
                        # Passei no construtor, os atributos da classe pai e ainda o classe filha   
    def __init__(self, marca, modelo, preco,ram,memoria_interna,camera_traseira):
        super().__init__(marca, modelo, preco) #chama o construtor da classe pai, ou seja, a classe da qual essa classe herda os atributos
        self.ram = ram
        self.memoria_interna = memoria_interna
        self.camera_traseira = camera_traseira
    
    def desconto(self):
        return self._preco * 0.15      
Sansung = Telefone('Sansung','Ultra',1800)
print(Sansung.desconto())
Sansung.fazer_uma_ligacao(992401158)
Sansung.desconto()

Iphone = Smarthphone('Iphone',13,8000,32,128,True)
print(Iphone)
print(vars(Iphone))         