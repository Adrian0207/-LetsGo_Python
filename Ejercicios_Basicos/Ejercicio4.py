'''Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.'''
num1 = int(input('Valor 1...'))
num2 = int(input('Valor 2...'))

suma = num1 + num2
resta = num1 - num2
mult = num1 * num2
divi = num1 // num2 # division resultante de numeros enteros
divi2 = num1 / num2

print('Suma: ' + str(suma))
print('Resta: ' + str(resta))
print('Multiplicacion: ' + str(mult))
print('Division Entero: ' + str(divi)) 
print('Division Real: ' + str(divi2)) 