#Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se for digitado
#impar desconsidere-o
soma = 0
for i in range (1, 7):
    num = int(input("Insira o {}º valor: ".format(i)))
    if num%2 == 0:
        soma += num
print("O resultado da soma dos numeros PARES digitados é: {}".format(soma))
