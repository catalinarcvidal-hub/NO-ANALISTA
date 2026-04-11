#C)	Desarrolle un programa que permita ingresar 3 notas y al finalizar despliegue el promedio.

#Variable

nota_1 = 0.0
nota_2 = 0.0
nota_3 = 0.0
cant_de_notas = 3
promedio = 0.0


#Entrada

nota_1 = float(input("Ingrese la primera nota : "))
nota_2 = float(input("Ingrese la segunda nota : "))
nota_3 = float(input("Ingrese la tercera nota : "))

promedio = (nota_1 + nota_2 + nota_3) / cant_de_notas

#Salida

print("El promedio de las tres notas es de",promedio,".")




