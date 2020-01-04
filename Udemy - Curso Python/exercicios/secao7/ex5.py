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
