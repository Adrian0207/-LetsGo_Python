'''
Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. 
El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) 
y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.
'''

velocidad1 = float(input('Velocidad del carro 1 en km/h...'))
velocidad2 = float(input('Velocidad del carro 2 en km/h...'))

distancia= float(input('Distancia entre los carros en km...'))


tiempo = distancia / (abs(velocidad1 - velocidad2))
tiempo = tiempo * 60 



print('Lo alcanzara en: ' + str(tiempo) + ' minutos')