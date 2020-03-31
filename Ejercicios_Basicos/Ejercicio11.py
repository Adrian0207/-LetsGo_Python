'''
Pide al usuario dos números y muestra la "distancia" entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
'''

distancia1 = float(input('Distancia 1...'))
distancia2 = float(input('Distancia 2...'))

distancia_total = abs(distancia1 - distancia2)

print('La distancia entre ' + str(distancia1) + ' y ' + str(distancia2) + ' es: ' + str(distancia_total))