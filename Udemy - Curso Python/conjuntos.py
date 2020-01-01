"""
Conjuntos

- Conjuntos, em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matematica

- No Python, ps conjuntos são chamados de Sets

Da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados.

Utiliza-se conjuntos, quando precisamos analisar elementos, mas não é importante com a ordenação deles
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionarios) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor

# Definindo um conjunto:
# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Valores repetidos
print(s)
print(type(s))
# Obs.: Ao criar um conjunto, se for adicionado um valor já existente, sera ignorado sem gerar erros

# Forma 2 - Mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto
if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Importante lembrar, que alem de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 12, 1, 44, 5, 2, 34]
print("Lista {} com {} elementos".format(lista, len(lista)))

tupla = (99, 2, 34, 23, 12, 1, 44, 5, 2, 34)
print("Tupla {}, com {} elementos".format(tupla, len(tupla)))

dicionario = {}.fromkeys([99, 2, 34, 23, 12, 1, 44, 5, 2, 34], 'dict')
print("Dicionario {} com {} elementos".format(dicionario, len(dicionario)))

conjunto = {99, 2, 34, 23, 12, 1, 44, 5, 2, 34}
print("Conjunto {} com {} elementos".format(conjunto, len(conjunto)))
# Tuplas e listas aceitam dois elementos, já dicionários, e conjuntos (set) não aceitam

# Assim como todo outro conjunto em Python, podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

for valor in s:
    print(valor)


# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feita ou museu e os visitantes
# informam manualmente a cidade de onde vieram

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))
# Agora precisamos saber quantas cidades distintas temos

# Podemos utilizar um set para isso:
print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4)
s.add(4)  # duplicidade não gera erro
print(s)

# Remover elementos em um conjunto
s = {1, 2, 3}
# Forma 1
print(s)
s.remove(3)  # Não é indice, informamos o valor a ser removido
print(s)
# Obs.: Caso o valor não seja encontrado, sera gerado o erro KeyError

# Forma 2
s.discard(2)
print(s)
# Obs.: Se o valor não for encontrado, nenhum erro é gerado

# Copiando um conjunto para outo
s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Metodos matematicos de conjuntos
# Imagine que temos dois conjuntos, um contendo estudantes do curso Python e um contendo estudantes
# do curso de Java
estudantes_python = {'Marcos', 'Patricia', 'Elen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe '|'
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes de um curso, que não estão em outro
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, valor maximo*, valor minimo* e tamanho
# * se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}
print(max(s))
print(min(s))
print(sum(s))
print(len(s))
"""