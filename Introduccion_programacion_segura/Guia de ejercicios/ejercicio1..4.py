"""
Crear un algoritmo en diagrama de flujo que al 
ingresar dos números imprima el mayor de ellos  
o IGUALES si son iguales. 
"""
a = 0
b = 0

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

if a == b :
    print(f"El número {a} y {b} son iguales.")
    
else:
    if a > b:
        print(f"El mayor entre {a} y {b} es: {a}")
    else:
        print(f"El mayor entre {a} y {b} es: {b}")

