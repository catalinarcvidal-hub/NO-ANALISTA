#2.Desarrolle un programa que permite
# ingresar 3 números y desplegar siempre el mayor.
#nota: Depurar siempre con 3 numeros distintos.

a = 0
b = 0
c = 0

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

if a > b :
    if a > c :
        print("El número mayor es A")
    else :
        print("El número mayor es C")
else : 
    if b > c :
        print("El número mayor es B")
    else :
        print("El numero mayor es C")

# complejidad ciclomatica 
# Metodologia agil
