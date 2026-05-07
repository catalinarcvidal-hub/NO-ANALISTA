"""
Desarrolle un programa que permita 
ingresar 5 numeros y al finalizar retorne
cuantos numeros pares ingreso el usuario.

Nota: Solo se deben considerar numeros positivos.
"""
c = 1
x = 0
p = 0


while c <= 5:
    x = int(input("Ingrese un número positivo: "))
    if x < 0:
        print("El número ingresado debe ser positivo, vuelva a ingresar un número válido.")
    else: 
        c = c + 1
        if x % 2 == 0:
            p = p + 1

print(f"Usted a ingresado un total de {p} número pares.")


    