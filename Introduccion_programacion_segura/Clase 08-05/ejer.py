"""
Desarrolle una funcion que reciba dos 
números como argumento y me retorne un true si esos dos números son amigos
(la suma de los divisores del primer numero es igual que del segundo).
"""

divisibles = 0

for x in range(1, numero + 1):
    if numero % x == 0:
        divisibles = divisibles + 1

if divisibles == 2:
    return True
else:
    return False

"""
1. Desarrolle una función que retorne el factorial(factorial de 4 es 1*2*3*4) de un número.
"""