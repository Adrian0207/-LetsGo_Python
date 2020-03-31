'''
Programa que declare una lista y la vaya llenando de números hasta que 
introduzcamos un número negativo. Entonces se debe imprimir el vector 
(sólo los elementos introducidos).
'''
lista = []

while True:
    num = int(input('Ingrese un numero...'))
    if num < 0:
        break
    lista.append(num)

for i in lista:
    print(i, end = ' ')
