"""
EJERCICIOS BASICOS PROPUESTOS.

2.- 
Supongamos que el I.P.C. de los meses de Febrero y Marzo fueron 0.3% y 0.6% respectivamente. Crear un algoritmo en diagrama 
de flujo que muestre el valor de un producto actualizado y la diferencia de precio entre el mes de febrero y Marzo. 
"""
#Valor Producto
vp = 0
#Valor Febrero
vf = 0
#Valor Marzo
vm = 0
#Diferencia en pesos entre el precio de febrero y marzo.
dif = 0

vp = int(input("Ingrese el valor inicial del producto: "))

vf = vp + (vp * 0.003)
print(f"El valor del producto en Febrero es de {vf}")
vm = vf + (vf * 0.006)
print(f"El valor del producto en Marzo es de {vm}")
dif = vm - vf
print(f"La diferencia del precio entre el mes de febrero y marzo es de {dif} pesos.")