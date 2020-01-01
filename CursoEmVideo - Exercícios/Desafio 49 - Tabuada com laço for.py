# Refaça o desafio 09, mostrando a tabuada de um numero que o usuario escolher, so que agora usando um laço for
num = int(input("Insira um número para ver sua tabuada: "))
for c in range (1, 11):
    print("{} X {:2} = {}".format(num, c, num*c))
