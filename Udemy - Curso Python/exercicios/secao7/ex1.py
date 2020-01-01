a = [1, 0, 5, -2, -5, 7]
print(a)  # ALTERNATIVA A

soma = a[0] + a[1] + a[5]
print(soma)   # ALTERNATIVA B

a.insert(4, 100)
print(a)  # ALTERNATIVA C

for valor, posicao in enumerate(a):
    print(f'Na posição {valor}, temos o valor {posicao}')  # ALTERNATIVA D

