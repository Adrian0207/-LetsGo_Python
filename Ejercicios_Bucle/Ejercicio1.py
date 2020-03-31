num = int(input('Ingresa un numero...'))
fact = 1

for i in range(2, num + 1):
    fact *= i

print('El resultado del factorial del numero es: ' + str(fact))
        
