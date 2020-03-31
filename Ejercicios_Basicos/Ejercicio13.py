'''
Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica. 
Python3 no tiene ninguna función predefinida que permita calcular la raíz cúbica, ¿Cómo se puede calcular?
'''

num = int(input('Ingrese un numero...'))

num_raiz_cuadrada = num ** (1/2)
num_raiz_cubica = num ** (1/3)

print('Raiz cuadrada: ' + str(num_raiz_cuadrada))
print('Raiz cubica: ' + str(num_raiz_cubica))