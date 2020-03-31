'''Diseñar una función que calcule el área y el perímetro de una circunferencia. 
Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.'''

def Validacion(cad):
    while True:
        try:
            num = int(input(cad))
            break
        except ValueError:
            print('Ingrese un numero valido!!!')
    return num

def calcular(radio):
    perimetro = float( 2 * PI * radio)
    area = float(PI * radio ** 2)

    print('El perimetro es: %.2f y el area es: %.2f' % (perimetro, area))
    
PI = 3.14

radio = Validacion('Ingrese el radio del circulo...')
calcular(radio)
    