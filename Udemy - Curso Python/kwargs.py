"""
**kwargs

Pode chamar este parâmetro com outro nome como **xis, mas por convenção chamamos de **kwargs

O **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras
em um dicionario

# Exemplo


def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')
    print(kwargs)


cores_fav(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs: Os parametros *args e **kwargs não são obrogatórios
cores_fav()

# Exemplo mais complexo


def comprimento_especial(**kwargs):
    if 'marcos' in kwargs and kwargs['marcos'] == 'python':
        return 'Voce recebeu um cumprimento Pythonico'
    elif 'marcos' in kwargs:
        return f"{kwargs['marcos']} Marcos!"
    return 'Não tenho certeza quem voce é'


print(comprimento_especial())
print(comprimento_especial(marcos='python'))
print(comprimento_especial(marcos='oi'))
print(comprimento_especial(marcos='epecial'))

# Nas funções podemos ter (NESTA ORDEM):
 - Parâmetros obrigatórios;
 - *args;
 - Parâmetros default (não obrigatório);
 - **kwargs

 def funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


funcao(8, 'Julia')
funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
funcao(34, 'Felipe', eu='Não', voce='Vai')
funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Importância de manter essas ordem dos parâmetros

# Função com a ordem correta de parâmetros
# def mostra_info(a, b, *args, instrutor='Marcos', **kwargs):
#     return [a, b, args, instrutor, kwargs]

# print(mostra_info(1, 2, 3, sobrenome='Marinho', cargo='Instrutor'))

print()


# Função com a ordem incorreta de parâmetros
def mostra_info(a, b, instrutor='Marcos', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='Marinho', cargo='Instrutor'))

# Desempacotamento com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Marcos', 'sobrenome': 'Marinho'}
print(mostra_nomes(nome='Marcos', sobrenome='Marinho'))  # Funciona
# print(mostra_nomes(nomes))  # Apresenta TypeError, necessário desempacotar os elementos com '**'
print(mostra_nomes(**nomes))
"""