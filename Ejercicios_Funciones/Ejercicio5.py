'''Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.'''

def Validacion(cad):
    while True:
        try:
            num = int(input(cad))
            break
        except ValueError:
            print('Ingrese un numero valido!!!')
    return num

def calcularMaxMin(lista):
    maxi = lista[0]
    mini = lista[0]
    for i in range (1, len(lista)):
        if lista[i] > maxi:
            maxi = lista[i]
        if lista[i] < mini:
            mini = lista[i]
    print('Maximo: %d, Minimo: %d' %(maxi, mini))

lista_num = []

while True:
    numero = Validacion('Ingrese un numero...')
    if numero >= 0:
        lista_num.append(numero)
    else:
        break

calcularMaxMin(lista_num)

    