'''
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
en cuenta su sueldo base y comisiones.
'''
sueldo_base = float(input('Sueldo base...'))
comision = 0.1

venta1 = float(input('Valor venta 1...'))
venta2 = float(input('Valor venta 2...'))
venta3 = float(input('Valor venta 3...'))

comision_total = (venta1 + venta2 + venta3) * comision

sueldo_total = comision_total + sueldo_base

print('Comision total: %.2f' % comision_total)
print('Sueldo total: %.2f' % sueldo_total)