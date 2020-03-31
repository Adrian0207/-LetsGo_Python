'''
Ask the user to enter three points and find whether they are collinear.
In the above question, if the points are not collinear then find the type of
triangle formed by them (equilateral, isosceles or scalene).
In the above question, check if the triangle is right angled.
'''
x1 = float(input('ingrese una coordenada x del punto 1: '))
y1 = float(input('ingrese una coordenada y del punto 1: '))

x2 = float(input('ingrese una coordenada x del punto 2: '))
y2 = float(input('ingrese una coordenada y del punto 2: '))

x3 = float(input('ingrese una coordenada x del punto 3: '))
y3 = float(input('ingrese una coordenada y del punto 3: '))

resp = x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)
if(resp == 0):
    print('Es colineal')
else:
    h1 = float(((x1-x2)**2 + (y1-y2)**2)**.5)
    h2 = float(((x2-x3)**2 + (y2-y3)**2)**.5)
    h3 = float(((x3-x1)**2 + (y3-y1)**2)**.5)
    print('distancia 1 ',h1,' distancia 2 ',h2,' distancia 3 ',h3)
    if(h1 == h2 and h1 == h3 and h2 == h3):
        print('Equilatero')
    elif((h1 == h2) and (h1 != h3) or (h1 == h3) and (h1 != h2) or (h2 == h3) and (h2 != h1)):
        print('Isoceles')
    else:
        print('Escaleno')

    a = float(h1**2 + h2 **2);b = float(h1**2 + h3**2); c = float(h2**2 + h3**2)
    #print(a,' ' ,b, ' ',c)
    if(a >= h3 or b >= h2 or c >= h1):
        print('Es tringulo rectangulo')
    
