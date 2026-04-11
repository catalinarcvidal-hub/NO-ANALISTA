#D)	Para bajar 1 kg. de peso tenemos que trotar 30 minutos y realizar 100 abdominales, 
# realice un sistema donde se ingrese la cantidad de peso que se desea bajar y el sistema
# le entregue cuantos minutos debe trotar y la cantidad de abdominales que debe ejecutar.

#Variable

kg_a_bajar = 0.0
minutos_de_trote_por_kg = 30
cant_de_abdominales_por_kg = 100
minutos_de_trote_a_realizar = 0
cant_de_abdominales_a_realizar = 0


#Entrada

kg_a_bajar = float(input("Ingrese los kilos que desea bajar: "))

minutos_de_trote_a_realizar = minutos_de_trote_por_kg * kg_a_bajar
cant_de_abdominales_a_realizar = cant_de_abdominales_por_kg * kg_a_bajar

#Salida

print("Usted desea bajar",kg_a_bajar," kilos, por tanto, debe realizar",minutos_de_trote_a_realizar,"minutos de trote y",cant_de_abdominales_a_realizar,"abdominales para cumplir su meta.")
