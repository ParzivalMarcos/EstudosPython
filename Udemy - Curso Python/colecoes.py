"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays), em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos de colocar QUALQUER tipo de dados.

Linguagens, C/Java: Arrays
    - Possuem tamanho e tipo de dado fixo;
    Em outras palavras, nestas linguagens, se for criado um array, do tipo
    int, e com tamanho 5, este array, será SEMPRE do tipo inteiro e poderá ter sempre no máximo
    5 valores.

Já em Python:
- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando
elementos.
- Qualquer tipo de dado: Não possuem tipo de dado fixo; Ou seja, podemos colocar qualquer tipo de
dado.

As listas em python, são representadas por colchetes: []

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['M', 'a', 'r', 'c', 'o', 's', ' ', 'L', 'i', 'm', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('Marcos Lima')

# Podemos checar se determinado valor esta contido na lista
if 8 in lista4:
    print("Encontrei o numero 8")
else:
    print("Não encontrei o numero 8")

# Ordenar uma lista
lista1.sort()
print(lista1)

# Contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('a'))

# Adicionar elementos em listas
# Para adicionar elementos em listas, utilizamos a função append
# Com append, conseguimos adicionar apenas 1 elemento por vez
print(lista1)
lista1.append(42)
print(lista1)

# Podemos colocar mais de um elemento, inserindo mais uma lista, como elemento unico (sublista)
lista1.append([8, 3, 1])
print(lista1)

if [8, 3, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Lista não encontrada")

# Adiciona cada elemento da lista, como valor adicional a lista
lista1.extend([123, 44, 67])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do indice
lista1.insert(2, "Novo valor")
print(lista1)

append & extend - SEMPRE NO FINAL DA FILA
insert - INSERE EM UMA POSIÇÃO DESEJADA DA LISTA

# Podemos juntar duas listas
lista6 = lista1 + lista2
print(lista6)
lista1.extend(lista2)
print(lista1)

# Inverter uma lista
## forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

## forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista
lista6 = lista2.copy()
print(lista6)

# Contar quantos elementos existem dentro da lista
print(len(lista5))

# Podemos remover facilmente o ultimo elemento de uma lista
# obs.: o pop não apenas remove o ultimo elemento, mas também retorna o valor dele
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# obs.: os elementos a direita deste indice, serão realocados para a esquerda
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos (zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista
# Exemplo 1
curso = "Programação em python: essencial"
print(curso)
curso = curso.split()
print(curso)

# Obs: Por padrão, o split separa os elementos da lista pelo espaço entre elas

# Exemplo 2
curso = "Programação,em,python:,Essencial"
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ["Programação", "em", "Python", "Essencial"]
print(lista6)

# Abaixo: Pega a lista6, coloca espaço em cada elemento e transforma em uma string
curso = " ".join(lista6)
print(curso)

# Abaixo: Pega a lista6, coloca cifrão em cada elemento e transforma em uma string
curso = "$".join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, "Geek", "d", [1, 2, 3], 452368543]
print(lista6)
print(type(lista6))

# Iterando sobre listas
# Exemplo 1 - Utilizando for
soma = 0
for elemento in lista1:
    print(elemento)
    soma += elemento
print(soma)

# Exemplo 2 - Utilizando while
carrinho = []
produto = ""
while produto != 'sair':
    produto = input("Adicione um produto na lista ou digite 'sair' para sair: ")
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Fazemos acesso aos elementos de forma indexada
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])

# Fazer acesso aos elementos de forma indexada inversa
# para entender melhor o indice negativo, pense na lista como uma roda, onde o final de um elemento
# esta ligado ao inicio da lista
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerando indice
# cores = list(enumerate(cores))
# print(cores)

# Gerar indice em um for
# for indice, cor in enumerate(cores):
#    print(indice, cor)

# Outros metodos
# Encontrar o indice de um elemento na lista
# Obs: Caso não tenha este elemento na lista, será apresentado erro ValueError
numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice esta o valor 6
print(numeros.index(6))

# Em qual indice esta o valor 9
print(numeros.index(9))

print(numeros.index(5))  # Retorna o indice do primeiro elemento encontrado

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # Buscando a partir do indice 1

# Obs: Caso não tenha este elemento na lista, será apresentado erro ValueError
# print(numeros.index(5, 4))  # Buscando a partir do indice 4

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o indice do valor 8, entre os indices 3 a 6

# Revisão de slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro inicio
lista = [1, 2, 3, 4]
# Iniciando no indice 1 e pegando todos os elementos restantes
# Podemos passar numeros negativos, e tambem, toda a lista com "::"
print(lista[1:])

# Trabalhando com slice de lista com o parâmetro fim
# No exemplo, ele começa no indice 0, e vai ate o indice 2-1
print(lista[:2])

# Trabalhando com slice de lista com o parâmetro passo
print(lista[1::2])  # Começa em 1, e vai ate o final de 2 em 2

# Invertendo valores em uma lista

nomes = ["Marcos", "Marinho"]
nomes[0], nomes [1] = nomes[1], nomes[0]
print(nomes)

nomes = ["Marcos", "Marinho"]
nomes.reverse()
print(nomes)

# soma*, valor maximo*, valor minimo*, tamanho
# *Se os valores forem todos inteiros ou reais

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista))  # soma
print(max(lista))  # maximo valor
print(min(lista))  # minimo valor
print(len(lista))  # tamanho da lista

# Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))
# Desempacotamento de listas
lista = [1, 2, 3]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
# Se tivermos um numero diferente de elementos na lista, ou variaveis para receber os dados
# teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)

nova.append(4)
print(lista)
print(nova)
# Ao utilizar o copy(), copiamos os dados da lista para uma nova lista, mas elas ficaram
# totalmente independentes, ou seja, modificando uma lista, não afeta a outra. Isso em Python
# é chamado de Deep Copy, ou copia profunda

# Forma 2 - Shallow Copy
lista = [1, 2, 3]
print(lista)

nova = lista
print(nova)

nova.append(4)
print(lista)
print(nova)
# Utilizando a copia via atribuição, e copia os dados da lista para a nova
# No entanto, ao modificar uma das listas, esta modificação reflete em ambas as listas
# isso em Python, é chamado de Shallow Copy
"""