'''
Realiza un programa que reciba una cantidad de minutos y muestre por 
pantalla a cuantas horas y minutos corresponde.
'''
import math

min_ingreso = int(input('Valor en minutos...'))

convertir = min_ingreso / 60
parte_decimal, parte_entera = math.modf(convertir)
horas = int(parte_entera)
minutos = int(parte_decimal * 60)

print(str(min_ingreso) + ' minutos son ' + str(horas) + 'horas  y ' + str(minutos) + ' minutos')