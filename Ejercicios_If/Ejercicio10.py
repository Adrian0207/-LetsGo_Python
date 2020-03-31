x1 = int(input('Coordenada x1...'))
y1 = int(input('Coordenada y1...'))
x2 = int(input('Coordenada x2...'))
y2 = int(input('Coordenada y2...'))

r1 =  int(input('Radio 1...'))
r2 =  int(input('Radio 2...'))
distancia = ((x2 - x1)**2 + (y2 - y1) ** 2)**(1/2)

if distancia > (r1 + r2):
    print('Circunferencias exteriores')

elif distancia == (r1 + r2):
     print('Circunferencias tangentes exteriores')

elif distancia < (r1 + r2) and distancia > abs(r1 - r2):
     print('Circunferencias secantes')

elif distancia == abs(r1 + r2) and distancia > abs(r1 - r2):
     print('Circunferencias tangentes interiores')

elif distancia > 0 and distancia < abs(r1 + r2):
     print('Circunferencias interiores')

elif distancia == 0:
    print('Circunferencias concétricas')

else:
    print('ERRROR')