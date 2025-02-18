class Animal:
    
    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        
class Peixe(Animal):
    raca = '' 
    
class Papagaio(Animal):
    cor = ''
    
class Zoologico:
    def __init__(self):
        self.animais_dict = {}
    
    def add_animal(self,animal):
        self.animais_dict[animal.nome] = animal.categoria

    def total_categoria(self,categoria):
        result = 0
        for animal in self.animais_dict.values():
            if animal == categoria:
                result +=1
        return f'Nosso ZOO tem {result} quantidade de categoria {categoria}'

zoo = Zoologico()
peixe = Peixe('Nemo','Anfibio')
print(vars(peixe))
papagaio = Papagaio('Piu-Piu','Ave')
print(vars(papagaio))

zoo.add_animal(peixe)
zoo.add_animal(papagaio)
print(zoo.total_categoria('Anfibio'))
print(zoo.total_categoria('Ave'))

            