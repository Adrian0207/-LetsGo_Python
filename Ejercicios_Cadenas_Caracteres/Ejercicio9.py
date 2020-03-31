'''Realizar un programa que compruebe si una cadena contiene una subcadena.
Las dos cadenas se introducen por teclado.'''

cadena = input('Ingrese una cadena...')
subcadena = input('Ingrese una cadena...')
if subcadena in cadena:
    print(subcadena + ' se encuentra en ' + cadena)
else:
    print(subcadena + ' no se encuentra en ' + cadena)