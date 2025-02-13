# 1 - Liste valores de 0 - 10 que sejam menores do que 4
# for i in range(10):
#     if i < 4:
#         print(i)
# Fazendo isso com list Comprehension
# new_list = [i for i in range(10) if i<4]      

games_list = ['ario',"DK Country","Luigis Mansion","Kirby"]

# Retornando apenas os jogos que tem a letra a
list = [i for i in games_list if 'a' in i]
print(list)

for i in games_list:
    if "a" in i:
        print(i)