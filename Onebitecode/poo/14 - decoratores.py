import time
import requests

# Criando um decorator calcular_tempo
def calcular_tempo(funcao):
    def wrapper():
        tempo_inicial = time.time()
        funcao()
        tempo_final = time.time()
        print(f'A duração foi de {tempo_final - tempo_inicial}')
    return wrapper


@calcular_tempo # Passando o decorator para calcular o tempo de execução
def pegar_cotacao_dolar():
    link = f'https://economia.awesomeapi.com.br/last/USD-BRL'
    requisicao = requests.get(link)
    requisicao = requisicao.json()
    print(requisicao['USDBRL']['bid'])

pegar_cotacao_dolar()    