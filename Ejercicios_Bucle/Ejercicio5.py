cadena = input('Cuantos numeros va a ingresar?...')
cadena = cadena.upper()

for i in cadena:
    if i == 'A' or i == 'E' or i =='I' or i == 'O' or i == 'U':
        print ('VOCAL')
    else:  
        print ('NO VOCAL') 

  