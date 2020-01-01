# Faça um programa que calcule a soma de todos os numeros impares que são multiplos de 3 e que se encontram no intervalo
# entre 1 e 500
soma = 0
valor = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        valor += 1
        soma += c
print("A soma de todos os {} valores solicitados é {}".format(valor, soma))
