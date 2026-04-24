"""
EJERCICIOS BASICOS PROPUESTOS.
2.- Supongamos que el I.P.C. de los meses de Febrero y Marzo fueron 0.3% y 0.6% respectivamente. Crear un algoritmo en diagrama 
de flujo que muestre el valor de un producto actualizado y la diferencia de precio entre el mes de febrero y Marzo. 
"""
#Valor atual/presente
precio_inicial = 0
#Valor Febrero
precio_febrero = 0
# 0.3% IPC en ferebro se divide en 100 y nos da el 0.003
ipc_febrero = 0.003
#Valor Marzo
precio_marzo = 0
# 0.6% IPC en ferebro se divide en 100 y nos da el 0.006
ipc_marzo = 0.006
#Diferencia en pesos entre el precio de febrero y marzo.
diferencia = 0

print("¿Quieres saber cuanto ha subido el precio del producto de tu elección entre Febrero y Marzo? Elige uno e ingresa su precio.")
print()

precio_inicial = int(input("Ingrese el valor del producto: "))

if precio_inicial > 0:
    precio_febrero = precio_inicial + (precio_inicial * ipc_febrero)
    print(f"El precio en febrero con el IPC de 0.3% es de ${precio_febrero}")

    precio_marzo = precio_febrero + (precio_febrero * ipc_marzo)
    print(f"El precio en Marzo con el IPC de 0.6% es de ${precio_marzo}")
    
    diferencia = precio_marzo - precio_febrero
    print(f"La diferencia del precio entre el mes de febrero y marzo es de ${diferencia} pesos.")
else: 
    print("Monto invalido, debe ser mayor a cero.")