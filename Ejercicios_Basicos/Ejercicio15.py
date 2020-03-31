'''
Dadas dos variables numéricas A y B, que el usuario debe teclear, 
se pide realizar un algoritmo que intercambie los valores de ambas variables y 
muestre cuanto valen al final las dos variables.
'''

A = int(input('Valor de A...'))
B = int(input('Valor de B...'))

C = A; A = B; B = C

print('El valor nuevo de A es:' + str(A) + ' y el valor nuevo de B es: ' + str(B))