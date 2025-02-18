class Pessoa:
    
    def __init__(self,idade,nome):
        self._nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,valor):
        if not isinstance(valor,str):
            raise TypeError('Nome deve ser uma string')
        self._nome = valor    
        
pessoa = Pessoa('Gabriel',22)
print(vars(pessoa))        