valorMin = int(input('Valor minimo...'))
valorMax = int(input('Valor maximo...'))


for i in range(valorMin, valorMax + 1):
    if i % 2 == 0:
        print (i, end=' ')
