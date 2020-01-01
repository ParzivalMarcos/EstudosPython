"""
Modulo Collections - Default Dict

# Recap Dicionarios
dicionario = {'curso' : 'Programação em Python'}
print(dicionario)
print(dicionario['curso'])

Default Dict -> Ao criar um dicionario utilizando-0, nós informamos um valor defalut.
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido.
Caso tentamos acessar uma chave que não existe, essa chave será criada e o valor default será atribuido

Obs.: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores

# Fazendo import
from collections import defaultdict
dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python'
print(dicionario)
print(dicionario['outro'])
print(dicionario)

help(defaultdict)
"""


