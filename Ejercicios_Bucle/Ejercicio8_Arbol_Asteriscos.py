'''
Crear un árbol de asteriscos trabajando con bucles anidados. 
Un árbol de asteriscos tiene una forma de diamante, considerando el número de espacios y caracteres de asterisco (*), centrados en cada línea. 
El número de asteriscos aumenta en uno para cada nueva línea hasta la parte media, después el número de asteriscos disminuye en uno para cada nueva 
línea hasta que llegue al final.
'''

while True:
    altura = int(input('Ingrese el tamaño del arbol mayor a 3: '))
    if altura >= 3:
        break
impar_max = 2 * altura - 1
num_asterisco = 1
arbol = ''
tronco = ''

for i in range(altura):
    for j in range(altura - i + 1):
        arbol += ' '
    if num_asterisco <= impar_max:
        for j in range(num_asterisco):
            arbol += '*'
    print(arbol)
    num_asterisco += 2
    arbol = ''


for i in range (altura):
    tronco += ' '
tronco += '***'

for i in range (3):
    print(tronco)
        
