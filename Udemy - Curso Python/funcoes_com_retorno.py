"""
Funções com retorno

numeros = [1, 2, 3]
ret = numeros.pop()  # Removendo o ultimo elemento de uma lista
print(ret)
print(numeros)

Obs.: Quando uma função nao retorna nenhum valor, o retorno é None


# Exemplo
def quadrado_de_7():
    return 7 * 7


# variavel recebendo o retorno da função
res = quadrado_de_7()
print(res)

print(f'{quadrado_de_7()}')

# Retornando variavel
def quadrado_de_7():
    teste = 7 * 7
    return teste

res = quadrado_de_7()
print(res)

def funcao():
    return 1, 2, 3, 4

print(funcao())
# Desempacotando retorno de varios valores
num1, num2, num3, num4 = funcao()
print(num1, num2, num3, num4)

from random import random
# Criar uma função de cara ou coroa


def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())

refatorando função
def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())
"""

from random import random
# Criar uma função de cara ou coroa


def joga_moeda():
    # Gera um numero pseudo-randomico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())



