# 1.- En un terminal salen dos buses con destino a la ciudad de Valdivia, transportan a 35 pasajeros cada uno, el valor del pasaje fue de $5.500. Cuál es la recaudación obtenida.
cant_de_buses = 0
cant_de_pax_por_bus = 0
val_pass = 0
recaudacion_total = 0

#Entrada

cant_de_buses = int(input("Ingrese la cantidad de buses que realizaron el recorrido a Valdivia: "))
cant_de_pax_por_bus = int(input("Ingrese la cantidad de pasajeros con los que sale cada bus: "))
val_pass = int(input("Ingrese el valor del pasaje:"))

recaudacion_total = val_pass * cant_de_buses * cant_de_pax_por_bus

#Salida

print("En un terminal salen",cant_de_buses, "buses y cada bus lleva a bordo", cant_de_pax_por_bus, "pasajeros. Cada uno de los pasajeros pago un valor de", val_pass, "pesos, por lo que, el total de recaudación de ese trayecto fue de", recaudacion_total,"pesos.")



