'''
Crea una lista e inicalizala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra 
sus elementos  por la pantalla.
'''
lista = []

for i in range(0,5):
    cadena = input('Ingrese una cadena...')
    lista.append(cadena)

lista_inversa = lista[::-1] #invierto la lista 
for i in lista_inversa:
    print(i, end=' ')



        