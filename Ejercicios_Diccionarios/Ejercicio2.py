'''Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.'''

cad = input('Ingrese una cadena...')

dic = {}
for i in range(len(cad)):
    valor = cad.count(cad[i])
    if cad[i] not in dic:
        dic[cad[i]] = valor

for clave, valor in dic.items():
    print(clave, '\t', valor)