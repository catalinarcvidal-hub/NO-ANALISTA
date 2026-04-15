"""
Desarrolle un programa que permita ingresar 3 números
y desplegarlos de forma descendente.

"""
n1 = 0
n2 = 0 
n3 = 0 
menor : 0
mediano : 0
mayor : 0

n1 = int(input("Ingrese un número: "))
n2 = int (input("Ingrese otro número: "))
n3 = int(input("Ingrese un último número: "))

if n1 < n2 :
    menor = n1
    if n2 < n3 : 
        mediano = n2
        mayor = n3
    else:
        mediano = n3
        mayor = n2
else:
    if n2 < n1:
        menor = n2
        if n1 < n3:
            
