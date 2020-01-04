"""
List Comprehension
(parte 1)

- Utilizando List Comprehension pode-se gerar novas lists com dados processados a partir de outro iteravel.

# Sintaxe da List Comprehension
[ dado for dado in iteravel ]

# Exemplos
numeros = [1, 2, 3, 4, 5]
res = [numero * 10 for numero in numeros]
print(res)

Para melhor compreensão dividindo a expressão acima em duas partes:
- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

res =[numero / 2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

# List Comprehensions versos loop

# loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numeros_dobrado = numero * 2
    numeros_dobrados.append(numeros_dobrado)
print(numeros_dobrados)

# List Comprehensions
print([numero * 2 for numero in numeros])

# Outros exemplos

# 1
nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['maria', 'julia', 'pedro', 'gulherme', 'vanessa']
print([caixa_alta(amigo) for amigo in amigos])
print([amigo.title() for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])


(parte 2)

Podemos adicionar estruturas condicionais logicas, as List Comprehension
"""
# Exemplo 1
numeros = [200, 27, 302, 4, 5, 6]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)


# Refatorando

# Qualquer numero par módulo de 2 é 0 e 0 em Python é False, not False = True
pares = [numero for numero in numeros if not numero % 2]
# Qualquer modulo impar modulo de 2 é 1, e em python 1 é true
impares = [numero for numero in numeros if numero % 2]
print(pares)
print(impares)

# Exemplo 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

