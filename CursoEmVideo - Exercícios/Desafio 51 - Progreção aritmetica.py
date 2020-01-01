# Desenvolva um prigrama que leia o primeiro termo, e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progresão
print("PROGRESSÃO ARITMETICA")
termo = int(input("Insira o primeiro termo: "))
razao = int(input("Insira a razão: "))
decimo = termo + (10-1) * razao
for i in range(termo, decimo+razao, razao):
    print("{} → ".format(i), end='')
print("FIM")
