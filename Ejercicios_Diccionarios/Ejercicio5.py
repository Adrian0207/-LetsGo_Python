'''Escribir un programa que implemente una agenda. En la agenda se podrán guardar nombres y números de teléfono. El programa nos dará el siguiente menú:
> Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto. 
Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
>Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
>Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
>Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario.'''

dic = {'Adrian' : '0960863638', 'Soyf' : '0998654086', 'Anny' : '0999989798', 'Mele' : '0999920021', 'Adriana' : '0986655246'}

while True:
    print('1 -> Añadir/Modificar')
    print('2 -> Buscar')
    print('3 -> Borrar')
    print('4 -> Listar')
    print('5 -> Salir')
    opc = int(input('Opcion...'))

    if opc == 1:
        nombre = input('Ingrese el nombre...')
        if nombre in dic:
            print('El usuario ' + nombre + 'ya existe, su numero es: ' +str(dic[nombre]))
            verificacion = input('Desea modificarlo?(Y/N)...')
            if verificacion.upper == 'Y':
                dic[nombre] = input('Ingrese su numero telefonico...')
        else:
            dic[nombre] = input('Ingrese su numero telefonico...')
    elif opc == 2:
        nombre = input('Ingrese el nombre...')
        for clave, numero in dic.items():
            if nombre in clave:
                print(clave, '\t', numero)

    elif opc == 3:
        nombre = input('Ingrese el nombre...')
        if nombre in dic:
            eliminar = input('Desea eliminar a ' + nombre + '?(Y/N)...')
            if eliminar.upper == 'Y':
                del dic[nombre]
        else:
            print('El usuario no existe')
    elif opc == 4:
        for nombre, numero in dic.items():
            print(nombre, '\t', numero)
    elif opc == 5:
        print('Gracias!!!')
        break
    else:
        print('Opcion invalida')
