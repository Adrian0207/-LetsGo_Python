'''Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.'''
fahr = float(input('Valor en Fahrenheit...'))

celsius = (fahr - 32) * (5/9)

print('Celsius: ' + str(celsius))