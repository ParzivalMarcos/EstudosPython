"""
Sorted

Não é a mesma coisa que a função sort() que só funciona em listas, ja o Sorted, pode ser utilizado em qualquer iteravel

mais uma diferença entre sort() e sorted()
A função sorte() modifica uma lista, o sorted() retorna uma lista, e nao modifica a original

# Exemplo

numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))

print(numeros)

# Adicionando parametros ao sorted()
numeros = [6, 1, 8, 2]

print(sorted(numeros, reverse=True))  # Ordena do maior para o menor

# Utilizando o sorted() para coisas mais complexas

usuarios = [
    {'username': 'Marcos', 'tweets': ['Eu adoro chocolate', 'Eu adoro pizzas']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'Diogo', 'tweets': ['Eu gosto de gatos', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': []},
    {'username': 'Jubileu', 'tweets': ['Voce nao sabe, nem eu']}
]

print(usuarios)

# Ordenando pelo username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))

# Ultimo exemplo

musicas = [
    {"titulo": "Wiz Kaliffa", "tocou": 3},
    {"titulo": "System of a Down", "tocou": 10},
    {"titulo": "50 Cent", "tocou": 5},
    {"titulo": "Metalica", "tocou": 7},
    {"titulo": "Michael Jackson", "tocou": 9},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))
"""

