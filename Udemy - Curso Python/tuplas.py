"""
Tuplas (tuple)

Tuplas, são bastante parecidas com listas.
Existem basicamente duas diferenças:
1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutaveis, o que significa que ao se criar uma tupla, ela não muda.
Toda operação em uma tupla, gera uma nova tupla

# Cuidado 1: As tuplas são representadas por (), mas:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento
tupla3 = (4)  # Não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # É uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 4,
print(tupla5)
print(type(tupla5))
# Conclusão: podemos concluir que tuplas são definidas pela ',' e não pelo uso do parênteses

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de tupla
tupla = ("Marcos", "Lima", "Marinho")
nome1, nome2, nome3 = tupla
print(nome1)
print(nome2)
print(nome3)
# Gera ValueError, se colocar um número diferente de elementos para desempacotar, similar as listas

# Metodos para adição e remoção de elementos nas tuplas, não existem, dado o fato das tuplas, serem imutaveis

# Soma*, valor maximo*, valor minimo*, e tamanho
tupla = (1, 2, 3, 4, 5, 6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tuplas são imutaveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)

tupla1 = tupla1 + tupla2  # Tuplas são imutaveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento esta contido na tupla
tupla = (1, 2, 3)
print(1 in tupla)

# Iterando sobre uma tupla
tupla = (1, 2, 3)
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ("a", "b", "c", "d", "a", "b")
print(tupla.count("a"))

teste = tuple("Marcos Lima")
print(teste)

print(teste.count("a"))

# Dicas na utilização de tuplas
# Deve-se utilizar tuplas, sempre que não precisa modificar os dados contidos em uma coleção

# Exemplo 1
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print(meses)

# Acesso de elementos de uma tupla é semelhante a uma lista
print(meses[5])

# Iterar com while
i = 0
while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual indice um elemento esta na tupla
print(meses.index("Junho"))
# Obs.:Caso o elemento não exista, sera gerado erro

# Slicing
# Tupla(inicio, fim, passo)
print(meses[0:])

Porque utilizar tuplas:
 - Tuplas são mais rapidas do que listas
 - Tuplas deixam seu código mais seguro - Uma vez que trabalhar com elementos imutaveis, traz segurança para o codigo

# Copiando uma tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla, não temos o caso de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)
print(outra)

nova += outra

print(nova)
print(outra)
"""