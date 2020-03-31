'''Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a partir de los datos guardados en el diccionario. 
Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta..'''

dic = {'manzana' : 1.0, 'pera' : 0.5, 'mandarina' : 0.25}
fruta = input('Frutra vendida...')
cantidad = int(input('Cantidad vendida...'))

precio_total = dic[fruta] * cantidad

print('La fruta',fruta, 'tiene un valor total de:',precio_total)