'''Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.'''
cateto1 = int(input('Valor cateto 1...'))
cateto2 = int(input('Valor cateto 2...'))

hipotenusa = ((cateto1 ** 2) + (cateto2 ** 2))**(1/2)

print('La hipotenusa es %.2f' % hipotenusa)