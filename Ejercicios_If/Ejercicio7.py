base = int(input('Base...'))
exp = int(input('Exponente...'))

if exp == 0:
    print(1)
elif exp > 0:
    print(base ** exp)
else:
    exp *= -1
    print('1/' + str(base ** exp))