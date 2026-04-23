"""
Desarrolle un programa que permita ingresar 10 números positivos, si el usuario ingresa un número negativo mostramos 
"Error en el ingreso" no se considera como número valido, al finalizar debemos mostrar la suma de los números ingresados.
"""

numero = 0
contador = 1
suma = 0

while contador <= 10:
    numero =  int(input("Ingresa un número: "))

    #Para saber que es positivo, debe ser 0 o mayor.
    if numero > 0:
        suma = suma + numero
        contador = contador + 1
    else:
        print("Error en el ingreso, reintente")

print(f"La suma de los números ingresados es {suma}")




