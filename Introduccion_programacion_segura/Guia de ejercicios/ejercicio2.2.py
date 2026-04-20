"""
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por 
las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
en cuenta su sueldo base y comisiones. 
"""

sueldo_base = 0
# Este intervalo representa la comision del 10% en decimal.
comision = 10 / 100
#Este intervalo es para representar el monto total de ventas realizadas en el mes.
ventas = 0
#Este intervalo representa el monto de comision que tendra por las ventas del mes
comision_total_ventas = 0

total = 0

sueldo_base = int(input("Ingrese el monto de su sueldo base: "))
ventas = int(input("Ingrese el monto total de ventas que realizo en el último mes: "))

comision_total_ventas = ventas * comision
total = sueldo_base + comision_total_ventas

print(f"El presente mes realizo un total de ${ventas} en ventas de las cuales recibira ${comision_total_ventas} por concepto de comisión. El total de su sueldo base mas las comisiones es de ${total} .")
