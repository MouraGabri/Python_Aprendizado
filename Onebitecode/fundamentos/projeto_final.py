listas_time = {}

def adicionar_time(time_futebol):
    listas_time[time_futebol] = [] # Adiciona uma chave (nome do time) 
    #com uma lista vazia de jogadores
 
 
def cadastrar_time():
        times_cadastrados = 0
        total_times_cadastrados = int(input("Informe a quantidade de times para cadastrar:")) 
        while times_cadastrados < total_times_cadastrados:
            nome_time = input("Nome do time:").lower()
            adicionar_time(nome_time)
            times_cadastrados += 1
        print('------------------------------------')
        print(f'Times cadastrados até o momento:{listas_time}')  
            
def remover_time():
    remover_time = input("Nome do time para remover:").lower()
    listas_time.pop(remover_time)
    print('------------------------------------')
    
def listar_times():
    print('------------Lista de times------------------------')
    for index, (time,jogadores) in enumerate (listas_time.items()):
        print(f'{index} : Times cadastrados: {time}, {len(jogadores)}', end= ' | ')
        
    print()    
        
def cadastrar_jogadores():
    print('------------- Cadastrar Jogadores-------------')
    total_jogadores_cadastrados = int(input('Quantidade de Jogadores para cadastrar:'))
    jogadores_cadastrados = 0
    tentativa_sistema = 3
    tentativas = 0
    
    while jogadores_cadastrados < total_jogadores_cadastrados:
        buscar_time = input("nome do time:")
        if buscar_time in listas_time:
            cadastrar_jogador = input("Nome do jogador:")
            listas_time[buscar_time].append(cadastrar_jogador)
            jogadores_cadastrados +=1
            break
        else:
            print('Time não encontrado')
            tentativas +=1
            print(f'Tentativa:{tentativas}')
        if tentativas == tentativa_sistema:
            print('saindo do sistema...')
            exit()        
                # Fiz o append, pois os valores de um dicionario são no formato de uma lista e assim consigo usar o append
                # print(listas_time.items())
                
def remover_jogador():
    print('------------------------------------')
    encontrar_time = input('Nome do time:')
    if encontrar_time in listas_time:
        print(f'Jogadores: {listas_time[encontrar_time]}')
        remover_jogador = input('Nome do Jogador para remover:')
        if remover_jogador in listas_time[encontrar_time]:
            listas_time[encontrar_time].remove(remover_jogador)
            print(f'O jogador {remover_jogador} foi removido do time {encontrar_time}')
            
def listar_jogadores_do_time():
    time = input('Informe o nome do time:')
    if time in listas_time:
        print(f'Jogadores: {listas_time[time]}') 
        
        
cadastrar_time()
remover_time()
cadastrar_jogadores()
listar_times()
listar_jogadores_do_time()
remover_jogador()

    
    