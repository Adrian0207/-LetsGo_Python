'''Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. 
Cada alumno puede tener distinta cantidad de notas. Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas 
con las notas de cada alumno.'''

dic = {}

alumnos = int(input('Cuantos alumnos?...'))
for i in range(0, alumnos):
    nombre = input('Nombre...')
    num_notas = int(input('Cuantas notas?...'))
    notas = []
    for j in range(0, num_notas):
        notas.append(int(input('Ingrese la nota N° ' + str(j + 1) + ' : ')))
    dic[nombre] = notas

for nombre, notas in dic.items():
    print(nombre, '\t', notas)
