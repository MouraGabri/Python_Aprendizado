import json

# 1 - Strings para Dicionários
person = '{"name":"Rodrigo", "languages":["Python","PHP"]}'
person_dict = json.loads(person)
print(person_dict)

# 2 - Convertendo dicionario para json
person_json = json.dumps(person_dict)
print(person_json)

# 3 - Formatando em Json
print(json.dumps(person_dict, indent=4, sort_keys=True))

# 4 - Salvando Json em TXT
with open("person.txt","w") as json_file:
    json.dump(person_dict,json_file)

# 5 - Lendo um json externo
with open("iris.json", "r") as f:
    data = json.load(f)
    print(data)