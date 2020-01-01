"""
Modulo Collections: Ordered Dict

OrderedDict > É um dicionário que nos garante a ordem de inserção dos elementos.

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave = {chave} : valor = {valor}')

# Entendendo a diferença entre dict e orderer dict
# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # True -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict
odict1 = OrderedDict(dict1)
odict2 = OrderedDict(dict2)

print(odict1 == odict2)  # False -> Já que no OrderedDict a ordem dos elementos importa
"""

