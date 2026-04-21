"""
EJERCICIOS BASICOS PROPUESTOS.
2.- Supongamos que el I.P.C. de los meses de Febrero y Marzo fueron 0.3% y 0.6% respectivamente. Crear un algoritmo en diagrama 
de flujo que muestre el valor de un producto actualizado y la diferencia de precio entre el mes de febrero y Marzo. 
"""
#Valor atual/presente
vp = 0
#Valor Febrero
vf = 0
#Valor Marzo
vm = 0
#Diferencia en pesos entre el precio de febrero y marzo.
dif = 0

print("¿Quieres saber cuanto ha subido el precio del producto de tu elección entre Febrero y Marzo? Elige uno e ingresa su precio.")
vp = int(input("Ingrese el valor del producto: "))

print(f"El precio del producto hoy es ${vp} que son ${diferencia} mas caros que los de Febrero.")
vm = vf + (vf * 0.006)
print(f"El valor del producto en Marzo es de {vm}")
dif = vm - vf
print(f"La diferencia del precio entre el mes de febrero y marzo es de {dif} pesos.")