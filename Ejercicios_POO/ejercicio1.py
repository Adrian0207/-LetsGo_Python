'''
Crear una clase Persona que tenga como atributo Nombre, Edad y DNI.
Aplique el uso de decoradores.
Crear una funcion que permita verificar si es mayor a 18 años
Usar la funcion __str__ para imprimir el nombre y la edad 
'''
class Persona():
    def __init__(self,nombre="",edad=0,dni=""):
        self.__nombre=nombre
        self.__edad=edad
        self.__dni=dni
    
    '''Decorador de nombre'''
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre=nombre

    '''Decorador de edad'''
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,edad):
        self.__edad=edad

    '''Decorador de DNI'''
    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self,dni):
        self.__dni=dni
    
    def esMayorDeEdad(self):
        if self.edad >= 18:
            print('Es mayor de edad')
        else:
            print('Es menor de edad')

    def __str__(self):
        return 'Nombre: {} Edad: {}'.format(self.nombre, self.edad)


p1 = Persona()
print(p1)
    
p2 = Persona('Pepe', 5); print(p2); p2.esMayorDeEdad()
p3 = Persona('Jorge', 18); print(p3); p3.esMayorDeEdad()
p4 = Persona('Maria', 30); print(p4); p4.esMayorDeEdad()







