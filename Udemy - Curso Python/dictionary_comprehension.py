"""
Dictionary Comprehension

# Sintaxe
{chave:valor for valor in iterável}

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}  # itens(), retorna uma lista de tuplas do dicionario
print(quadrado)

# Gerando dicionarios a partir de uma lista, também vale para tupla ou set(conjunto)
numero = [1, 2, 3, 4, 5, 1]
ao_quadrado = {valor: valor ** 2 for valor in numero}
print(ao_quadrado)

# Gerando um dicionario a partir de uma string e uma lista
chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo com logica condicional

numeros = [1, 2, 3, 4, 5]
res = {num: ('par' if not num % 2 else 'impar') for num in numeros}
print(res)
"""
