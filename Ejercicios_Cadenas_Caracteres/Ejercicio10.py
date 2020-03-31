'''
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra 
palíndroma es aquella que se lee igual adelante que atrás.
'''
cadena = input('Ingrese una cadena...')
cadena_invertida = ''

for i in range(len(cadena) - 1, -1 , -1):
    cadena_invertida += cadena[i]

if cadena == cadena_invertida:
    print(cadena + ' es palindromo')
else:
   print(cadena + ' no es palindromo')