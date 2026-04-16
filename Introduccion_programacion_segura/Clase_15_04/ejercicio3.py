"""
Desarrolle un programa que permita ingresar mil numeros al usuario, 
al terminar despliegue la suma de ellos.

"""
n_us = 0
total = 0
n_ing = 0

n_us_in = int(input("Ingrese un número: "))


while n_ing <= 4:
    print(n_ing)
    n_us_in = int(input("Ingrese un número: "))
    n_ing = n_ing + total

total = n_us_in + n_us
print (total)
