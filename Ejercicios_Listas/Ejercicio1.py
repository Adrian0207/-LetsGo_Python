'''
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10)
y posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''
import random

lista = []

for i in range(0,10):
    r = random.randint(1,10)
    lista.append(r)

for i in lista:
    print('Numero: %d, Cuadrado: %d, Cubo: %d' %(i, i ** 2, i ** 3))
        
