"""
Leer 10 números y obtener su cubo y su cuarta. 
osea multiplicar el numero 3 veces para el cubo y cuatro para la cuarta.
"""


numero = 0
contador = 1
cubo = 0
cuarta = 0

while contador <= 10:
    numero = int(input("Ingrese un número: "))
    cubo = numero * numero * numero
    cuarta = numero * numero * numero * numero
    print(f"El cubo del número es {cubo} y su cuarta es {cuarta}.")

    contador = contador + 1

print("Fin")








