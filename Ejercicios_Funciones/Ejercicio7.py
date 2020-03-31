'''Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y 
te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. 
Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login 
incremente este valor.'''

def Login():
    contador = 0
    while True:
        usuario = input('Usuario...')
        contra = input('Contraseña...')
        if usuario == 'usuario1' and contra == 'asdasd':
            print('Verdadero')
            break
        else:
            contador += 1
        print('Intento: ' + str(contador))

    
Login()
    