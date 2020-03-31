num1 = int(input('Valor 1...'))
num2 = int(input('Valor 2...'))
num3 = int(input('Valor 3...'))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print('%d , %d , %d' %(num1, num2, num3))
    else:
         print('%d , %d , %d' %(num1, num3, num2))
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print('%d , %d , %d' %(num2, num1, num3))
    else:
         print('%d , %d , %d' %(num2, num3, num1))
else:
    if num1 > num2:
        print('%d , %d , %d' %(num3, num1, num2))
    else:
         print('%d , %d , %d' %(num3, num2, num1))