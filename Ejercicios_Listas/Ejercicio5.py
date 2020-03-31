'''
Hacer un programa que inicialice una lista de números con valores aleatorios 
(10 valores), y posterior ordene los elementos de menor a mayor.
'''

import random

lista = []
lista_ordenada = []

for i in range(0,10):
    r = random.randint(1,10)
    lista.append(r)
lista.sort()

for i in lista:
    print(i, end = ' ')

