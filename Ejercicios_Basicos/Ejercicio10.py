'''
Un alumno desea saber cual será su calificación final en la materia de Algoritmos
Dicha calificación se compone de los siguientes porcentajes:
* 55% del promedio de sus tres calificaciones parciales.
* 30% de la calificación del examen final.
* 15% de la calificación de un trabajo final.
'''

promedio_parcial = float(input('Promedio de los tres parciales...'))
examen_final = int(input('Nota examen final...'))
trabajo_final = int(input('Nota trabajo final...'))

total_parcial = promedio_parcial * 0.55
total_examen = examen_final * 0.3
total_trabajo = trabajo_final * 0.15

calificacion = total_parcial + total_examen + total_trabajo

print('La calificacion total sobre 50 es: ' + str(calificacion))