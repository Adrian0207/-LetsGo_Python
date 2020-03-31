'''
Suponiendo que hemos introducido una cadena por teclado que representa una frase 
(palabras separadas por espacios), realiza un programa que cuente cuantas palabras tiene.
'''
cadena = input('Ingrese una frase...')
aux = cadena.split(' ')

print('La frase: ' + cadena + ' -> tiene ' + str(len(aux)) + ' palabras')