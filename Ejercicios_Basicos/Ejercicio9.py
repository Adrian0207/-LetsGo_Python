'''
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente 
desea saber cuanto deberá pagar finalmente por su compra.
'''

total_compra = float(input('Valor total de la compra...'))
descuento = total_compra - (0.15 * total_compra)

print('Total a pagar:%.2f ' + str(descuento))