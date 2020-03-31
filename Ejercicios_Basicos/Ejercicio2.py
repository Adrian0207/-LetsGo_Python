'''Calcular el perímetro y área de un rectángulo dada su base y su altura.'''
base = int(input('Valor de la base...'))
altura = int(input('Valor de la altura...'))

perimetro = (2 * base) + (2 * altura)
area = base * altura

print('El perimetro es %.2f' % perimetro)
print('El area es %.2f' % area)