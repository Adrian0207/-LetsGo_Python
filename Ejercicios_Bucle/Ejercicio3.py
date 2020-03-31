suma = 0
promedio = 0 
contador = 0

while True:
    num = int(input('Ingrese un numero...'))
    if num == 0:
        print('La suma es: %d y el promedio es %d' %(suma, promedio))
        break
    else:
        suma += num
        contador += 1
        promedio = suma / contador
    