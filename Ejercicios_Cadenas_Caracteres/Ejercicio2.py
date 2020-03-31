'''Realizar un programa que comprueba si una cadena leída por 
teclado comienza por una subcadena introducida por teclado.'''
cadena = input('Ingrese una cadena...')
subcadena = input('Ingrese una subcadena de inicio de la cadena...')

if cadena.startswith(subcadena):
    print(cadena + ' inicia con ' + subcadena)
else:
    print(cadena + ' no inicia con ' + subcadena)
        