"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma

# Refatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(4))
print(quadrado(5))
print(quadrado(2))
print(quadrado(7))

# Argumentos nomeados
# Utilizando nome dos parametros, nos argumentos, podemos utilizar qualquer ordem


def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'


nome = 'Marcos'
sobrenome = 'Marinho'

print(nome_completo(nome, sobrenome))
print(nome_completo(sobrenome, nome))

# Nomeando argumentos
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome=sobrenome, nome=nome))

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
        # return total  # return na posição errada, retornando em um caso de else, finalizando a função
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
"""

