"""
Todas as atividades em apenas um script Python
"""
import math


def secao7_exercicio_1():
    a = [1, 0, 5, -2, -5, 7]
    print(a)  # ALTERNATIVA A

    soma = a[0] + a[1] + a[5]
    print(soma)  # ALTERNATIVA B

    a.insert(4, 100)
    print(a)  # ALTERNATIVA C

    for valor, posicao in enumerate(a):
        print(f'Na posição {valor}, temos o valor {posicao}')  # ALTERNATIVA D


def secao7_exercicio_2():
    lista = []
    for i in range(1, 7):
        valor = input("Insira um valor: ")
        lista.append(valor)
    print(lista)


def secao7_exercicio_3():
    conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    lista = list(conjunto)
    print(lista)
    lista_ao_quadrado = []
    for i in range(0, len(lista)):
        quadrado = math.pow(lista[i], 2)
        lista_ao_quadrado.append(quadrado)
    print(lista_ao_quadrado)


def secao7_exercicio_5():
    """
    Leia um vetor de 10 posições. Contar e escrever quantos valores ele possui
    """

    vetor = [32, 4, 5, 6, 78, 7, 9, 3, 8]

    # Maneira convencional, utilizando laço for comum
    for i in vetor:
        if not i % 2:
            print(i)

    # Maneira utilizando list_comprehension
    print([numero for numero in vetor if not numero % 2])

    # Utilizando função

    def find_number_par(number):
        if not number % 2:
            return number

    for i in vetor:
        if not i % 2:
            print(find_number_par(i))


def secao7_exercicio_6():
    print('Faça um programa que receba do usuário um vetor com 10 posições.\n'
          'Em seguida deverá ser impresso o maior e menor elemento do vetor.\n\n')
    vetor = []
    for i in range(0, 10):
        numero = int(input(f'Insira o {i + 1}º número para o vetor: '))
        vetor.append(numero)
    print(f'Dos números que voce digitou, o maior número é {max(vetor)}\n'
          f' e o menor é {min(vetor)}')
    print(f'Todos os números digitados {vetor}')


def menu():
    print('Escolha uma seção de exercicios')
    print('Seção [4]\tSeção [5]\nSeção [6]\tSeção [7]\nSeção [8]')
    escolha = int(input('Opção: '))
    if escolha == 7:
        num_exercicio = int(input('Digite o numero do exercício da seção 7: '))
        if num_exercicio == 1:
            secao7_exercicio_1()
            continuar()  # -> Chamando função para sair ou não do programa
        elif num_exercicio == 2:
            secao7_exercicio_2()
            continuar()
        elif num_exercicio == 3:
            secao7_exercicio_3()
            continuar()
        elif num_exercicio == 5:
            secao7_exercicio_5()
            continuar()
        elif num_exercicio == 6:
            secao7_exercicio_6()
            continuar()
        else:
            print('Questão invalida!!')
            continuar()  # -> Chamando função para sair ou não do programa


def continuar():
    continua = int(input('Deseja continuar?\n[1] para SIM\n[Qualquer outro valor] para NAO\nOpção: '))
    if continua == 1:
        menu()
    else:
        print('Saindo do programa')
        return 0


# Iniciando programa
menu()
