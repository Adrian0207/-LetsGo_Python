contador = int(input('Cuantos numeros va a ingresar?...'))
contador0 = 0; contadorMax = 0; contadorMin = 0

for i in range (0, contador):
    num = int(input('Ingrese un numero...'))
    if num == 0:
        contador0 += 1
    elif num > 0:
        contadorMax += 1
    else:
        contadorMin += 1

print('Se ha ingresado: ' + str(contador0) + ' ves/ veces el numero 0, ' + str(contadorMax) + ' numero mayores a 0 y ' + str(contadorMin) + 'numero menores a 0')   