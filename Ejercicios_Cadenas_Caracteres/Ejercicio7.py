'''
Pide una cadena y dos caracteres por teclado (valida que sea un carácter), 
sustituye la aparición del primer carácter en la cadena por el segundo carácter.
'''

cadena = input('Ingrese una cadena...')

while True:
    charac1 = input('Ingrese una caracter...')
    if len(charac1) ==  1:
        break

while True:
    charac2 = input('Ingrese un segundo caracter...')
    if len(charac2) ==  1:
        break


print('Nueva cadena: ' + cadena.replace(charac1, charac2))
