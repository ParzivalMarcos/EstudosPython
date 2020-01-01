"""
Dicionários

Obs.: Em algumas linguagens de programação, os dicionários python, são conhecidos por mapas.
Dicionários, são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.
print(type({}))

Obs.: sobre dicionários
- Chave e valor são separados por dois pontos 'chave:valor'
- Tanto chave quanto valor pode ser qualquer tipo de dado.
- Podemos misturar tipos de dados.

# Criação de dicionarios
# Forma 1 (mais comum)
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py' : 'Paraguai'}
print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')
print(paises)
print(type(paises))

# Acessando elementos
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
print(paises['py'])

# Caso tentar fazer um acesso utilizando uma chave que não existe, teremos o erro: KeyError

# Forma 2 - Acessando via get - Recomendado
print(paises.get('br'))
print(paises.get('ru'))
# Caso o get não encontre o objeto com a chave informada, será retornado o valor None, e não serpa
gerado KeyError

# Forma classica
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
opcao = str(input("Digite a sigla de um pais para procurar: "))
pais = paises.get(opcao)
if pais:
    print(f"Pais {pais}, encontrado")
else:
    print('Pais não cadastrado')

# Podemos definir um valor padrão, caso não exista objeto relacionado a chave informada

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
opcao = str(input("Digite a sigla de um pais para procurar: "))
pais = paises.get(opcao, "Não encontrado")
print(f'{pais}')

# Podemos verificar se determinada chave se encontra em um dicionário
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']
else:
    print("error")

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive, lista, tupla, dicionario como
# chaves de dicionários.

# Tuplas são bastante interessantes de serem utilizadas como chave de dicionario, pois as mesmas
# são imutáveis
localidades = {
    (35.6895, 36.6917): "Escritorio em Tókio",
    (40.7128, 74.0060): "Escritorio em Nova York",
    (37.7749, 122.4194): "Escritorio em São Paulo",
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário

receita = dict(jan=100, fev=120, mar=300)
print(receita)
print(type(receita))

# Forma 1
receita['abr'] = 350
print(receita)

# Forma 2
novo_dado = {'mai': 500}
receita.update(novo_dado)  # receita.update({'mai': 500})
print(receita)

# Atualizando dados em um dicionário
# Forma 1
receita['mai'] = 550
print(receita)

# Forma 2
receita.update({'mai': 600})
print(receita)

# Conclusão 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário, é a mesma
# Conclusão 2: Em dicionários, NÃO podem possuir chaves repetidas

# Remover dados de um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
# Forma 1 - Mais comum

ret = receita.pop('mar')  # pop, remove o ultimo elemento, ou referencia-se pela chave
print(ret)
print(receita)

# Precisa sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado
# Ao remover um objeto, o valor deste, é sempre retornado.

# Forma 2
del receita['fev']  # Se a chave não existir, será gerado um KeyError
print(receita)

# Neste exemplo, o valor removido não é retornado.

    Carrinho de compras:
        produto 1:
            - nome;
            - quantidade;
            - preço.
        produto 1:
            - nome;
            - quantidade;
            - preço.

# 1 - Poderiamos utilizar uma lista para isso
carrinho = []
produto1 = ['Playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Teriamos que saber qual é o índice de cada informação no produto.

# 2 - Poderiamos utilizar tupla
produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('God of War 4', 1, 150.00)

carrinho = (produto1, produto2)
print(carrinho)
# Teriamos que saber qual é o índice de cada informação no produto.

# 3 - Utilizando dicionários
carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}
carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)
# Com dicionarios, facilmente adicionamos ou removemo produtos no carrinho, e em cada produto
# pode-se ter a certeza sobre cada informação

# Métodos de dicionários
d = dict(a=1, b=2, c=3)
print(d)

# Limpar dicionario (zerar dados)
d.clear()
print(d)

# Copiando um dicionário para outro
# Forma 1
novo = d.copy()  # Deep copy
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma 2
novo = d  # Shallow copy
print(novo)

novo['d'] = 4
print(d)
print(novo)

# Forma não usual de criação de dicionários
outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parâmetros: um iteravel e um valor.
# Ele vai gerar para cada valor do iterável, uma chave e irá atribuir a esta chave, o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""