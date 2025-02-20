"""Classe Cliente com nome, idade, email.
Classe ContaBancaria associada ao cliente.
Métodos para depósito e saque."""

class Cliente:
    
    def __init__(self,nome,idade,email):
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def __str__(self):
        return f'Dados do Cliente:\nNome:{self.nome}|Idade:{self.idade}|E-mail:{self.email}'    