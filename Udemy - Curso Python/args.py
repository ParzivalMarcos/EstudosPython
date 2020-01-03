"""
Entendendo o *args

- O *args é um parâmetro como outro qualquer, isso significa que voce poderá chamar de qualquer
coisa, desde que começe com asterisco

Exemplo:
*xis
Mas por convenção, utilizamos *args para defini-lo

O que é *args?

O parâmetro *args utilizado em uma função, coloca os valores extras informados como entrada em
uma tupla. Então, desde já lembre-se que tuplas são imutáveis

# Entendendo o args


def soma_todos(*args):
    return sum(args)


print(soma_todos())
print(soma_todos(1))
print(soma_todos(1, 2))
print(soma_todos(1, 2, 3))
print(soma_todos(2, 3, 4, 5))

def verifica_info(*args):
    if 'Marcos' in args and 'Marinho' in args:
        return f'Bem vindo {args[3]} {args[2]}'
    return 'Não conheço'


print(verifica_info())
print(verifica_info(1, True, 'Marinho', 'Marcos'))
print(1, 'Marinho', 3.145)


def soma_todos(*args):
    return sum(args)


# print(soma_todos())
# print(soma_todos(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos(*numeros))
# com o asterisco '*' informemos ao Python que estamos passando como argumento uma coleção de dads.
# desta forma, ele saberá que precisará antes desempacotar estes dados.
"""




