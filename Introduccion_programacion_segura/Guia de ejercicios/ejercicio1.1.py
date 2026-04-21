"""
EJERCICIOS BASICOS PROPUESTOS.

1.- 
Crear un algoritmo en diagrama de flujo  que al 
leer un número entero positivo (asuma que el número
cumple las condiciones), imprimir PAR si el número
es par e IMPAR si es impar.
"""
numero = 0

numero = int(input("Ingrese un número: "))

if numero > 0:
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
else:
    print("El número es invalido, ingrese un numero mayor a cero.")
=======
