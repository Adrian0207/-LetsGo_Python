'''
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos 
en el plano. Calcula y muestra la distancia entre ellos.
'''

x1 = int(input('Distancia x del punto 1...'))
y1 = int(input('Distancia y del punto 1...'))

x2 = int(input('Distancia x del punto 2...'))
y2 = int(input('Distancia y del punto 2...'))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2)**(1/2)



print('La distancia entre los puntos es: ' + str(distancia))