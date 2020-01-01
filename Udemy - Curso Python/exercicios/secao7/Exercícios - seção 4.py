"""
Leia uma temperatura em gras Celsius e apresente-a convertida em graus Fahrenheit
A formula é F = C*(9.0/5.0)+32, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius

Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius
A formula de conversão é: C = 5.0*(F-32)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit
"""
# grau, escolha = 0


def convert_celsius_fahrenheit(grau):
    f = grau * (9.0 / 5.0) + 32
    print(f'{grau}º Celsius, em Fahrenheit é {f}º ')


def convert_fahrenheit_celsius(grau):
    c = 5.0 * (grau - 32) / 9.0
    print(f'{grau}º Fahrenheit, em Celsius é {c}º')


def menu():
    grau = float(input("Insira qual a temperatura deseja converter: "))
    print("[1], para converter {} para Fahrenheit".format(grau))
    print("[2], para converter {} para Celsius".format(grau))
    escolha = int(input("Qual opção deseja escolher? "))
    if escolha == 1:
        convert_celsius_fahrenheit(grau)
    elif escolha == 2:
        convert_fahrenheit_celsius(grau)
    else:
        print("Opção errada, digite novamente")


menu()
