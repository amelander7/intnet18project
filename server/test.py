import json
# Converting a list of dict to JSON

lista = [{'id': 123, 'data': 'qwerty', 'indices': [1, 10]},
         {'id': 345, 'data': 'mnbvc', 'indices': [2, 11]}]

dict1 = {'user': 'Anton', 'password': '12345'}
dict2 = {'user': 'Hampus', 'password': '12345'}

lista = list()
lista.append(dict1)
lista.append(dict2)

print(lista)
json_lista = json.dumps(lista)

print(json_lista)
