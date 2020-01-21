"""
Min e Max

max() retorna o maior valor em um iteravel ou o maior de dois ou mais elementos
min() retorna o menor valor de um iteravel ou o menor de dois ou mais elementos

# Exemplo de dicionario
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(max(dicionario))  # Imprime a chave com maior valor

print(max(dicionario.values()))  # Imprime o maior elemento do dicionario

# Exemplo de dicionario
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(min(dicionario))  # Imprime a chave com menor valor

print(min(dicionario.values()))  # Imprime o menor elemento do dicionario

musicas = [
    {"titulo": "Wiz Kaliffa", "tocou": 3},
    {"titulo": "System of a Down", "tocou": 10},
    {"titulo": "50 Cent", "tocou": 5},
    {"titulo": "Metalica", "tocou": 7},
    {"titulo": "Michael Jackson", "tocou": 9},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# Imprimindo somente o titulo da musica mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
"""


