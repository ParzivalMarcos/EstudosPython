"""
Reduce

Obs.: A partir do python 3+ a função reduce() não é uma função Built-in (integrada)
Sendo necessário importar essa função a partir do módulo 'functools'

Para entender o reduce()

Imagine uma coleção de dados

dados = [a1, a2, a3, ..., an

função que recebe dois parâmetros:
def funcao(x, y)
    return x * y

A função reduce() recebe dois parametros: a função e o iterável
reduce(funcao, dados)

A função reduce() funciona da seguinte forma:
Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado
Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1,
mais o terceiro elemento e guarda o resultado
Sendo repetido até o final

Ou seja, em cada passo, ela aplica a função, passando como primeiro argumento, o resultado da aplicação anterior
no final, reduce() irá retornar o resultado final.

Alternativamente, poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4, an)

# Exemplo

# Multiplicando todos os numeros de uma lista
from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() precisamos de uma função que receba dois parâmetros
mult = lambda x, y: x * y

res = reduce(mult, dados)
res = reduce(lambda x, y: (x * y), dados)
print(res)
print(res)

# Utilizando um loop normal
res = 1
for n in dados:
    res = res * n
print(res)

"""