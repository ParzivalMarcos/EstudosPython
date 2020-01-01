from math import pow

conjunto = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
lista = list(conjunto)
print(lista)
lista_ao_quadrado = []
for i in range(0, len(lista)):
    quadrado = pow(lista[i], 2)
    lista_ao_quadrado.append(quadrado)
print(lista_ao_quadrado)
