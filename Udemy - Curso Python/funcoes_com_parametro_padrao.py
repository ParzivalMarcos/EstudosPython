"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional

def exponencial(numero, potencia=2):  # Tornando parametro 'potencia' com valor default 2
    return numero ** potencia


print(exponencial(3, 3))  # Eleva a potencia informada pelo usuario
print(exponencial(3))  # Por padrão eleva ao quadrado

# Obs.: Em Python, os parâmetros com valores default devem sempre estar no final da declaração

# Erro
def teste(potencia=1, num):
    return num ** potencia


print(teste(6))

# Outro Exemplo


def mostra_info(nome='Marcos', instrutor=False):
    if nome == 'Marcos' and instrutor:
        return 'Bem vindo instrutor!!'
    elif nome == 'Marcos':
        return 'Voce nao é instrutor'
    return f'Ola {nome}'


print(mostra_info())
print(mostra_info(instrutor=True))
print(mostra_info('Marinho'))

# Passando outras funções como parâmetros


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def sub(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, sub))

# Variaveis globais

total = 0
def incrementa():
    total = total + 1  # UnboundLocalError
    return total       # A variavel local esta sendo utilizada para processamento sem ter sido inicializada

total = 0


def incrementa():
    global total  # Informando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())

# Tendo funções que são declaradas dentro de funções, e também, tem uma forma especial de escopo de variavel


def fora():
    contador = 0

    def dentro():
        nonlocal contador  # Com 'nonlocal' informo que essa variavel esta na função anterior
        contador = contador + 1
        return contador
    return dentro()


print(fora())
"""



