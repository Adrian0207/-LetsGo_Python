'''
Programa que declare tres listas 'lista1', 'lista2' y 'lista3' de cinco 
enteros cada uno, pida valores para 'lista1' y 'lista2' y 
calcule lista3=lista1+lista2.
'''
lista_1 = []
lista_2 = []
lista_3 = []
valor = 5

for i in range (0, valor):
    num = int(input('Numero para la lista 1...'))
    lista_1.append(num)

for i in range (0, valor):
    num = int(input('Numero para la lista 2...'))
    lista_2.append(num)

for i in range(0, valor):
    lista_3.append(lista_1[i] + lista_2[i])
    print(lista_3[i], end = ' ')

