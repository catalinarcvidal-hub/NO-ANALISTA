"""
Calcular el promedio de un alumno que tiene 7 calificaciones en la materia de Diseño Estructurado de Algoritmos 
"""
nota1 = 0.0
nota = 0.0
promedio = 0.0
suma_notas = 0.0
contador = 1
ciclos = 7

print("Calculadora de promedio")
print("Ingresa hasta 7 notas y calcularemos tu promedio.")
print()

while contador <= ciclos :
    nota = float(input("Ingrese la nota: "))
    print(f"Has ingresado {contador} de {ciclos}.")
  
    suma_notas = ( suma_notas + nota ) 
    contador = contador + 1

promedio = suma_notas / 7
print(f"Su promedio es {promedio}")




