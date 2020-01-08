"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Mostrando os dados acima da media de uma coleção
# Dados coletados de algum sensor
dados = {1.3, 2.7, 0.8, 4.1, 4.3, -0.1}

# Calculando a media dos dados utilizando a função mean()
media = statistics.mean(dados)

# Obs.: Assim como a função map(), a filter() recebe dois parâmetros, sendo uma função e um iterável

res = filter(lambda x: x < media, dados)
print(list(res))
# print(f'novamente {list(res)}')  # Valor so fica na memoria após ser utilizada pela primeira vez

# Outra forma
print(list(filter(lambda x: (x > statistics.mean(dados)), dados)))

# Assim como na função Map, após serem utilizados os dados de filter() eles são excluidos da memória

# Retirando os campos vazios
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
print(paises)
res = filter(None, paises)
print(list(res))

# Outra forma
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

res = filter(lambda pais: len(pais) > 0, paises)
# res = filter(lambda pais: pais != '', paises)
print(list(res))
# ou
res = filter(None, paises)
print(list(res))

# map() -> Recebe dois parametros, uma função e um iteravel, e retorna um objeto mapeando a função para cada
# elemento do iteravel

# filter() -> Recebe dois parametros, uma função e um iteravel, e retorna um objeto filtrando apenas os elementos de
# acordo com a função

# A FUNÇÃO filter() sempre retorna True ou False (bool)
# A FUNÇÃO map() retorna um valor de acordo com a lista (int, str,...)

# Exemplo mais complexo
usuarios = [
    {'username': 'Marcos', 'tweets': ['Eu adoro chocolate', 'Eu adoro pizzas']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'bob123', 'tweets': []},
    {'username': 'Diogo', 'tweets': ['Eu gosto de gatos', 'Vou sair hoje']},
    {'username': 'Gal', 'tweets': []},
    {'username': 'Jubileu', 'tweets': ['Voce nao sabe, nem eu']}
]

# Filtrar os usuarios que estão inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)
"""
# Combinar filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria', 'May']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

# Primeira forma
instrutora = list(filter(lambda nome: len(nome) < 5, nomes))
print(list(map(lambda nome: f'Sua instrutora é {nome}', instrutora)))

# Segunda forma (uma linha)
print(list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes))))





