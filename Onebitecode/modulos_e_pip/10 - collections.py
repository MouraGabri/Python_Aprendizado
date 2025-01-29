from collections import Counter, namedtuple,deque
from operator import itemgetter

# 1 - Contar itens de uma lista
frutas = ["banana","laranja","Uva","Uva","Laranja","Abacaxi","Banana","Maça","Maça"]
print(Counter(frutas))

# 2 - Utilizando tupla nomeada
game = namedtuple('game',['name','price','note'])
g1 = game("Fifa23",90.50,8.5)
g2 = game("Resident Evil 4 Remake",300,10.0)
print(g1)
print(g2)

# 3 - Ordenando Dicionários
studants = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)

# 4 - Utilizando fila amba extremidades
deq = deque([20,40,60,80])
deq.appendleft(10)
deq.append(10)
print(deq)
deq.popleft()
deq.pop()
print(deq)



