import os
import datetime

# 1 Desligar o computador no windows
#os.system("shutdown /s") # Desliga em 60 s
#os.system("shutdown /s /t 0") #Desliga imediatamente

# 2 - Cancelar Desligamento
#os.system('shutdown /a') 

def desligar_uma_hora():
    os.system("shutdown /s t/ 3600")
    
def desligar_30_min():
    os.system("shutdown /s t/ 1800")    

def cancelar_desligamento():
        os.system("shutdown /a")    
cancelar_desligamento()        


os.system('shutdown /s /t 10')