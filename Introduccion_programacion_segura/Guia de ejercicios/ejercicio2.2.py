"""
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comision por 
las tres ventas que realiza en el mes y el total que recibirá en el mes tomando 
en cuenta su sueldo base y comisiones. 
"""

sueldo_base = 0
# Este intervalo representa la comision del 10% en decimal.
comision = 10
#Este intervalo es para representar el monto total de ventas realizadas en el mes.
ventas = 0
#Este intervalo representa el monto de comision que tendra por las ventas del mes
comision_total_ventas = 0

total = 0

sueldo_base = int(input("Ingrese el monto de su sueldo base: "))
ventas = int(input("Ingrese el monto total de ventas que realizo en el último mes: "))

if sueldo_base > 0 and ventas > 0:
    comision =  comision / 100
    comision_total_ventas = ventas * comision
    total = sueldo_base + comision_total_ventas
    print(f"El presente mes realizo un total de ${ventas} en ventas de las cuales recibira ${comision_total_ventas} por concepto de comisión. El total de su sueldo base mas las comisiones es de ${total} .")
else:
    print("Los valores ingresados deben ser mayor a $0")



"""
1. La fórmula general

Cómo calcular la comisión: Normalmente, la comisión es un porcentaje del total de tus ventas. Para obtener ese monto, multiplicas tus 
ventas por el porcentaje (dividido en 100):

{Comisiones} = {Ventas Totales} * {Comisión / 100} 

3. Ejemplo práctico

Supongamos los siguientes datos para un mes de trabajo:

Sueldo Base: $500.000
Ventas realizadas: $2.000.000
Porcentaje de comisión: 3% (esto equivale a 0,03)

Paso a paso:

Calculas la comisión: $2.000.000 * 0,03 = $60.000$.
Sumas al sueldo base: $500.000 + 60.000 = $560.000$.

Resultado: Tu sueldo total ese mes sería de $560.000.

"""