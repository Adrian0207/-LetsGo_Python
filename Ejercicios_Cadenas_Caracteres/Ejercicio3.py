'''
Pide una cadena y un carácter por teclado (valida que sea un carácter) 
y muestra cuantas veces aparece el carácter en la cadena.
'''
cadena = input('Ingrese una cadena...')
caracter = input('Ingrese un caracter...')

while caracter.isdigit():
    caracter = input('Ingrese un caracter...')
    if caracter.isdigit == False:
        break

print(cadena + ' contiene ' + str(cadena.count(caracter)) + ' vez/veces el caracter ' + caracter)

        