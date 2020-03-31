'''Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima.
 Crear un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media.
 El programa pedirá el número de días que se van a introducir.'''

def Temperatura(dia, mini, maxi):
    print('La media del dia %d es: %.2f' % (dia, ((mini + maxi) / 2)))

def Validacion(cad):
    while True:
        try:
            num = int(input(cad))
            break
        except ValueError:
            print('Ingrese un numero valido!!!')
    return num

dias = Validacion('Ingrese el numero de dias...')

for i in range(0, dias):
    mini = Validacion('Ingrese la temperatural minima del dia ' + str(i + 1) + '...')
    maxi = Validacion('Ingrese la temperatural maxima del dia ' + str(i + 1) + '...')
    Temperatura(i + 1, mini, maxi)