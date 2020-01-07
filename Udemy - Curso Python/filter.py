"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.


"""
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












