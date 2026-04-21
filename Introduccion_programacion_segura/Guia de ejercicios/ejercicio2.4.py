"""
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:

55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final. 
15% de la calificación de un trabajo final.
"""

parcial1 = 0.0
parcial2 = 0.0
parcial3 = 0.0
promedio_parciales = 0.0
examen_final = 0.0
trabajo_final = 0.0
nota_final = 0.0

parcial1 = float(input("Ingrese la primera nota: "))
parcial2 = float(input("Ingrese la segunda nota: "))
parcial3 = float(input("Ingrese la tercera nota: "))
examen_final = float(input("Ingrese la nota del examen final: "))
trabajo_final = float(input("Ingrese la nota del trabajo final: "))

#Calculo para sacar el promedio de las 3 notas.
promedio_parciales = (parcial1 + parcial2 + parcial3)/3

#Calculo para sacar el 55% del promedio y se guarde en la misma caja del promedio.
promedio_parciales = promedio_parciales * (55/100)

#Calculo para sacar el 30% al examen final
examen_final = examen_final * (30/100)

#Calculo para sacar el 15% al trabajo final
trabajo_final = trabajo_final * (15/100)

nota_final = (promedio_parciales + examen_final + trabajo_final)

print(f"Su nota final es {nota_final}")

# print(f"Su nota final es {nota_final.1f}") 
#Con el .1f lo que le indicamos es que el valor de la variable se redondeará automáticamente 
# el resultado al valor más cercano con un decimal.



