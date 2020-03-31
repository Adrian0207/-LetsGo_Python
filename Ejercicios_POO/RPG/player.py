'''
Clase Padre -> No necesita parentesis pero hereda de manera directa de object
'''
class Player:
    vocation = 'No vocation'
    spell = 'No Spell'
    movement_speed = 50

    '''
    kwargs = Cuando en una función uno de sus argumentos lleva un valor por defecto, 
    éste se convierte automáticamente en un keyword argument o argumento clave-valor, 
    tal como un diccionario
    '''

    '''__init__ es la inicializacion o constructor de la clase'''
    def __init__(self,**kwargs): #kwargs (keyword arguments) 
        self.name = input('Elije tu nombre: ')
        self.hit_points = kwargs.get('hit_points', 20)
        self.mana = kwargs.get('mana', 20)

    def cast_spell(self):
        return self.spell

    '''__str__ es el metodo que retorna un string para imprimir directamente lo que nosotros queramos de la clase'''
    def __str__(self):
       return '{} -> Vocation:{} -- Hit Points:{} -- Mana:{} -- Spell:{} -- Movement Speed:{} \n'.format(self.name,
            self.vocation, 
            self.hit_points,
            self.mana,
            self.cast_spell(),
            self.movement_speed)

'''Clase Hijo -> Herencia se lo ve en los parentesis, hereda de Player'''
class Mage(Player):
    vocation = 'Mage'
    spell = 'Fire Bolt'
    movement_speed = 20

    '''Sobre escritura del metodo cast spell'''
    def cast_spell(self):
        return '{} y Shadow Ball'.format(self.spell)

'''Clase Hijo -> Herencia se lo ve en los parentesis, hereda de Player'''
class Knigth(Player):
    vocation = 'Knigth'
    spell = 'Exori'
    movement_speed = 60

