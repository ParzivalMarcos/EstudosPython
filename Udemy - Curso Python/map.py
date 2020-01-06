"""
Map

Com map, fazemos mapeamento de valores para função.

import math


def are(r):
    # Calcula a area de um circulo com raio 'r'
    return math.pi * (r ** 2)


print(are(2))
print(are(5.3))

raios = [2, 5, 7.1, 8.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append((are(r)))
print(areas)

# Utilizando Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável. Retorna um Map Object
areas_map = map(are, raios)
print(areas_map)
print(type(areas_map))
print(list(areas_map))

# Forma 3
# Usando o mesmo exemplo com expressão lambda e Map
import math

raios = [2, 5, 7.1, 8.3, 10, 44]
areas_map = map(lambda r: math.pi * (r ** 2), raios)
print(areas_map)
print(type(areas_map))
print(list(areas_map))
print()

# Em uma linha
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# Obs.: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.


# Outro exemplo
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]
print(cidades)

# Convertendo as temperaturas das cidades de grau celcius em Farhenheit formula: f = 9/5 * c + 32

# Utilizando lambda e Map
far = map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)
print(list(far))
"""





