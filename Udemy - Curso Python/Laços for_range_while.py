"""
#For / range
nome = "Marcos Lima Marinho"
for i in nome:  # Passo por cada caractere da string
    print(i, end=' ')

print("\n")

for i, v in enumerate(nome):  # Enumero cada posição do for, retornando uma espécie de lista
    print("{}{} ".format(i, v), end='-> ')

print("\n")

for _, v in enumerate(nome):  # Com o underscore '_', estou descartando o valor do índice
    print("{} ".format(v), end='-> ')

print("\n")

for i in range(1, 10):  # Range numerica
    print(i, end='')

print("\n")

for v in enumerate(nome): # Outra forma do enumerate
    print(v, end='-> ')

for i in range(11):  # Outra forma do range, onde não especifica o começo, default é 0
    print(i)

# While
num = 1
while num < 10:
    print(num)
    num += 1

while True:
resposta = input("Digite sair, para fechar o programa: ")
if resposta == "sair":
    break
"""

