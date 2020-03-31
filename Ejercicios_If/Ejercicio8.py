nota = int(input('Nota...'))
edad = int(input('Edad...'))
sexo = input('Sexo (F/M)...')

if nota >= 5 and edad >= 18 and sexo == 'F':
    print('Aceptada')
elif nota >= 5 and edad >= 18 and sexo == 'M':
    print('Posible')
else:
    print('NO ACEPTADA')