#Faça um programa que mostre na ela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
#com uma pausa de 1 segundo entre eles.

import emoji
import time
import datetime

new_year = datetime.date.today().year + 1
explosao = 4 * emoji.emojize(':fireworks: ')
print('######## CONTAGEM REGRESSIVA PARA {} ########'.format(new_year))
for i in range(10, 0, -1):
    print(i)
    time.sleep(0.5)
print(emoji.emojize("Feliz {} {}".format(new_year, explosao)))
