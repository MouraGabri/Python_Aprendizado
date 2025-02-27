class Cliente:
    
    def __init__(self,nome,idade,cpf,bairro,rua,numero_apto_ou_casa,saldo_conta = 0.0):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.bairro = bairro
        self.rua = rua
        self.numero_apto_ou_casa = numero_apto_ou_casa
        self.saldo_conta = saldo_conta
        
    def __str__(self):
        return f'Cliente\nNome:{self.nome}\nIdade:{self.idade}\nCPF:{self.cpf}\nBairro:{self.bairro}\nRua:{self.rua}\nNúmero:{self.numero_apto_ou_casa}\nSaldo:{self.saldo_conta:.2f}'