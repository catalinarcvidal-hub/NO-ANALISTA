"""
Desarrolle un programa que permita ingresar mil numeros al usuario, 
al terminar despliegue la suma de ellos.

"""
contador = 1
numero = 0
total = 0

while contador <= 3:
    numero = int(input("Ingrese un número: "))
    total = total + numero
    print("Has ingresado", contador, "de 3.")
    contador = contador + 1
print("El total de la suma de los número ingresados es: ",total,)







