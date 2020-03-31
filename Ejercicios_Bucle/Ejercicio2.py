from random import randint #importar radint para crear numero aletorios enteros 

menor = 1
mayor = 10
secreto = randint(menor,mayor)
#print (secreto)
respuesta = int(input('Adivina el numero del ' + str(menor) + ' al ' + str(mayor) + ': ')) #trasformar los enteros en string en las cadenas
if respuesta == secreto:
    print('Ganaste!!! el numero era: ', str(respuesta))
else:
    while True:
        if mayor < respuesta or menor > respuesta   :
            print('El numero debe ser mayor a ' + str(menor) + ' y menor a' + str(mayor))
        elif respuesta == secreto:
            print('Ganaste!!! el numero era: ', str(respuesta))
            break 
        else:
            if secreto < respuesta:
                print('El numero es menor a ', str(respuesta))
                mayor = respuesta
            else:
                print('El numero es mayor a ', str(respuesta))
                menor = respuesta         
        respuesta = int(input('El numero esta entre el ' + str(menor) + ' y el ' + str(mayor) + ': '))
