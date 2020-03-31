'''Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro.
 Crea una función EsMultiplo que reciba los dos números, y devuelve si el primero es múltiplo del segundo.'''

def EsMultiplo(a,b):
    if a % b == 0:
        print('%d es multiplo de %d' %(a,b))
    else:
        print('%d No es multiplo de %d' %(a,b))

def Validacion():
    while True:
        try:
            num = int(input('Ingrese un numero...'))
            break
        except ValueError:
            print('Ingrese un numero valido!!!')
    return num

x = Validacion()
y = Validacion()

EsMultiplo(x,y)