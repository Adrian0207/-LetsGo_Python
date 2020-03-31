'''
Crear una lista de compras mediante una lista.
Usar funciones que permitan agregar, remover y ver los articulos.
'''
def agregarArticulos(listaArticulos):
    print('Ingrese los articulos que desee, para salir ingrese 0')
    while True:
        articulo = input('Ingrese un articulo...')
        if articulo != '0':
            listaArticulos.append(articulo)
        else:
            break
    return listaArticulos
        
def removerArticulos(listaArticulos):
    if len(listaArticulos) != 0:
        print('Ingrese el indice del articulo que quiere eliminar, para salir ingrese 0')
        while True:
            verArticulos(listaArticulos)
            opcion = int(input('Indice #...'))
            indice = opcion - 1
            if indice >= 0:
                del listaArticulos[indice]
            else:
                break
    else:
        print('No existen artículos en la lista\n')
    return listaArticulos

def verArticulos(listaArticulos):
    if len(listaArticulos) != 0:
        for i in range(len(listaArticulos)):
            print('%d) %s' % (i + 1, listaArticulos[i]))
    else:
        print('No existen artículos en la lista\n')
    

listaArticulos = []

print('Bienvendio a PYLista: ')
while True:
    print('1 -> Agregar Artículo\n' +
    '2 -> Remover Artículo\n'+
    '3 -> Ver Lista de Artículos\n'+
    '4 -> Salir')

    opcion = input('\nQue desea realizar?...')

    if opcion == '1':
        listaArticulos = agregarArticulos(listaArticulos)
    elif opcion == '2':
        listaArticulos = removerArticulos(listaArticulos)
    elif opcion == '3':
        verArticulos(listaArticulos)
    elif opcion == '4':
        break
    else:
        print('\n\nERROR, por favor elija una opción válida\n\n')
    

   