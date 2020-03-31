'''
Crea un programa que pida un número al usuario un número de mes 
(por ejemplo, el 4) y diga cuántos días tiene (por ejemplo, 30) 
y el nombre del mes. Debes usar listas. Para simplificarlo vamos 
a suponer que febrero tiene 28 días.
'''
lista_meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre','diciembre']
lista_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

mes = int(input('Numero de mes..'))

print('Mes: ' + lista_meses[mes - 1] + ' tiene: ' + str(lista_dias[mes - 1]) + ' dias' )












