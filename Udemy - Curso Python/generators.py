"""
Generators Expressions

Em aulas anteriores:
 - List Comprehension
 - Dictionary Comprehension
 - Set Comprehension

- Tuple Comprehension... seh chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# Realizando exemplo, utilizando Generators
nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']
print(any(nome[0] == 'C' for nome in nomes))  # Generator
print([nome[0] == 'C' for nome in nomes])  # List Comprehension

# Qual é a utiliza de getsizeof() -> Retorna a quantidade de bytes em memoria, do elemento passado como parâmetro
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' e 'Marcos Marinho' e um numero inteiro esta ocupando na memoria
print(getsizeof('Geek'))
print(getsizeof('Marcos Marinho'))
print(getsizeof(100))
print(getsizeof(True))
print(getsizeof(False))

from sys import getsizeof

# Gerando uma lista de numeros com list comprehension
list_comp = getsizeof([x * 10 for x in range(10)])

# Gerando uma lista de numeros com set comprehension
set_comp = getsizeof({x * 10 for x in range(10)})

# Gerando uma lista de numeros com dictionary comprehension
dict_comp = getsizeof({x: x * 10 for x in range(10)})

# Gerando uma lista de numeros com generator
gen_comp = getsizeof(x * 10 for x in range(10))
list_gen_comp = getsizeof(list(x * 10 for x in range(10)))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes\n'
      f'Set Comprehension: {set_comp} bytes\n'
      f'Dictionary Comprehension: {dict_comp} bytes\n'
      f'Generator Expression: {gen_comp} bytes')

# Iterando no Generator Expression

gen = (x * 10 for x in range(10))

for num in gen:
    print(num, end=' -> ')
"""

