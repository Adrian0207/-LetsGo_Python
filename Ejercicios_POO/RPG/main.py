import sys
sys.path.append("/..RPG/")#Ruta donde se encuentra nuestro archivo .py de las clases
import player

'''Intancia Mage'''
mage = player.Mage(hit_points = 10, mana = 20)#Usando diccionarios para pasar atributos a la clase a **kwargs
'''Intancia Knigth'''
knigth = player.Knigth(hit_points = 20, mana = 10)#Usando diccionarios para pasar atributos a la clase a **kwargs

'''Informacion Mage'''
print(mage)

'''Informacion Knigth'''
print(knigth)
