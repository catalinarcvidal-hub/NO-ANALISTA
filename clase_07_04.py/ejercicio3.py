# 3.- Desarrolle un programa que permite ingresar 
# 3 números y siempre los despliegue ascendentemente.
# NOTA: Depurar siempre con 3 numeros distintos.

a = 0
b = 0
c = 0
pmayor = ""
menor = ""
medio = ""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))


if pmayor a > b :
    a = "Posible mayor"
    if mayor a > c :
        a = "Mayor"
        if medio b > c : 
            b = "Medio"
        else :
            print("El valor medio es",medio,)

else : 
    b = "Posible mayor"
    if b > c :
        b = "Mayor"
    if medio a > c : 
            print("El valor medio es",a,)
        else :
            print("El valor medio es",c,)

 
print ("Ordenamos los números ingresados de manera ascendente:" , menor, medio, mayor,".")



    








