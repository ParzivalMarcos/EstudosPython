# Faça um programa que leia um numero inteiro, e diga se ele é ou não um numero primo.
num = int(input("Insira um numero: "))
if num%3 != 0:
    print("O {} digitado é primo".format(num))
else:
    print("O {} digitado não é primo".format(num))
