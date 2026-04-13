"""
Información del porcentaje por examen, calculo del promedio del ramo.

Evaluación 1 = 20%
Evaluación 2 = 35%
Evaluación 3 = 35%
Evaluación 4 = 10%
"""
ev1 = 0.0
ev2 = 0.0
ev3 = 0.0
ev4 = 0.0
pro = 0.0

ev1 = float(input("Ingrese la nota del primer examen: "))
ev2 = float(input("Ingrese la nota del segundo examen: "))
ev3 = float(input("Ingrese la nota del tercer examen: "))
ev4 = float(input("Ingrese la nota del cuarto examen: "))

#Calculo del promedio.
pro = (ev1 * 0.20) + (ev2 * 0.35) + (ev3 * 0.35) + (ev4 * 0.10)

if pro >= 4.0 :
  print("Vas por buen camino, sigue así")
else: 
  print("")

print(f"El promedio actual del ramo es: {pro}")

 


