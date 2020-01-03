"""
**kwargs

Pode chamar este parâmetro com outro nome como **xis, mas por convenção chamamos de **kwargs

O **kwargs exige que utilizemos parâmetros nomeados, e transforma esses parâmetros extras
em um dicionario

# Exemplo


def cores_fav(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')
    print(kwargs)


cores_fav(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

# Obs: Os parametros *args e **kwargs não são obrogatórios
cores_fav()

# Exemplo mais complexo


def comprimento_especial(**kwargs):
    if 'marcos' in kwargs and kwargs['marcos'] == 'python':
        return 'Voce recebeu um cumprimento Pythonico'
    elif 'marcos' in kwargs:
        return f"{kwargs['marcos']} Marcos!"
    return 'Não tenho certeza quem voce é'


print(comprimento_especial())
print(comprimento_especial(marcos='python'))
print(comprimento_especial(marcos='oi'))
print(comprimento_especial(marcos='epecial'))
"""



