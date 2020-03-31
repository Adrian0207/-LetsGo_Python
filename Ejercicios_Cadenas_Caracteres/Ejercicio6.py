'''
Realizar un programa que dada una cadena de caracteres por caracteres, genere 
otra cadena resultado de invertir la primera.
'''
cadena = input('Ingrese una cadena...')
cadena_invertida = ''

for i in range(len(cadena) - 1, -1 , -1):
    cadena_invertida += cadena[i]

print('Cadena invertida: ' + cadena_invertida)