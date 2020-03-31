'''Crear una función recursiva que permita calcular el factorial de un número. 
Realiza un programa principal donde se lea un entero y se muestre el resultado del factorial.'''

def Validacion(cad):
    while True:
        try:
            num = int(input(cad))
            break
        except ValueError:
            print('Ingrese un numero valido!!!')
    return num

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))
    
    