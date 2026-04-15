# 3.- Desarrolle un programa que permite ingresar 
# 3 números y siempre los despliegue ascendentemente.
# NOTA: Depurar siempre con 3 numeros distintos.

a = 0
b = 0
c = 0
mayor = ""
menor = ""
medio = ""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))


if a > b :
    mayor = a
    menor = b
    if a > c :
        mayor = a
        if b > c :
            medio = b
            menor = c
        else :
            medio = c
            menor = b 
    else:
         mayor = c
         medio = a
         menor = b      
else :
    if b > c :
        mayor = b
        medio = c
        if c > a :
            medio = c
            menor = a
        else :
            medio = a
            menor = c
    else: 
        if c > b :
            mayor = c
            if b > a :
                medio = b
                menor = a
            else: 
                medio = a
                menor = b
            

print(f"Ordenados de menor a mayor: {menor} , {medio} , {mayor}") 



    








