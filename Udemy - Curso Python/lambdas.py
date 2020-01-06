"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anonimas.

Geralmente aplicadas em filtragem e ordenação de dados

# Função em python
def soma(a, b):
    return a + b

def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Exemplo Lambda
lambda x: 3 * x + 1

# Utilizando a expressão lambda
calc = lambda x: 3 * x + 1
print(calc(4))

# Podemos ter expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo(' marcos ', 'MARINHO'))
print(nome_completo(nome=' MARCOS', sobrenome=' lima   '))

# Funções python, podemos ter nenhuma ou varias entradas. Em Lambdas também
teste = lambda: 'Como nao amar Python?'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(teste())
print(uma(5))
print(duas(2, 6))
print(tres(5, 1, 7))

# Usando a ordenação pelo primeiro nome
autores = ['Isaac Asimov', 'J. R. Tolkien', 'Agata Christie', 'Arthur C. Claire', 'Ernest Cline', 'Eduardo Sphor']
autores.sort()
print(autores)
print()

# Ordenando pelo sobrenome usando lambda
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
# Obs.: split() - separa os elementos
# -[-1] pega o ultimo elemento, no caso o sobrenome

# Função quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def gerar_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c
    # Retorna a função: f(x) = a * x ** 2 + b * x + c


teste = gerar_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(gerar_funcao_quadratica(3, 0, 1)(2))

"""

