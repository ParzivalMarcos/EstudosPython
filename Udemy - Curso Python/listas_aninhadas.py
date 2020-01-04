"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java/PHP) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimencionais (Marizes).

Em python temos Listas


# Exemplos
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
print(listas)
print(type(listas))

# Como fazer para acessar os dados
print(listas[0])
print(listas[0][1])  # 2
print(listas[2][1])  # 8
print(listas[2][-2])  # 8 - Numeros negativos voltam de tras pra frente

# Iterando com loops em uma linha aninhada
for lista in listas:
    for num in lista:
        print(num, end='  ')

# List Comprehension
[[print(num) for num in lista] for lista in listas]

# Gerando um tabuleiro/matriz 3 x 3
tabuleiro = [[numero for numero in range(1, 5)]for valor in range(1, 4)]
print(tabuleiro)


# Gerando jogadas para o jogo da velha
velha = [
    ['X' if not numero % 2 else 'O' for numero in range(0, 3)]
    for valor in range(0, 3)
]
print(velha)

# Gerando valor iniciais
print([
    ['*' for i in range(0, 3)]
    for j in range(0, 3)
])
"""
# Gerando um tabuleiro/matriz 3 x 3
tabuleiro = [[numero for numero in range(1, 5)]for valor in range(1, 4)]
print(tabuleiro)


# Gerando jogadas para o jogo da velha
velha = [
    ['X' if not numero % 2 else 'O' for numero in range(0, 3)]
    for valor in range(0, 3)
]
print(velha)

# Gerando valor iniciais
print([
    ['*' for i in range(0, 3)]
    for j in range(0, 3)
])






