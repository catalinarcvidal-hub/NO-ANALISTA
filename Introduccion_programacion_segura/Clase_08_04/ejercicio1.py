# Ejercicio.
# Desarrolle un programa que permita ingresar dos numeros si el 
# primero es mayor que el segundo despliegue la resta de ellos 
# si no, la multiplicacion y si son iguales se suma.

nro1 = 0
nro2 = 0
resta = 0


nro1 = int(input("Ingrese un número: "))
nro2 = int(input("Ingrese otro número: "))

if nro1 > nro2 :
    resta = nro1 - nro2
    print("La resta entre ambos números es",resta,)

else : 
    if nro2 > nro1 :
        mult = nro2 * nro1
        print("El producto entre ambos números es",mult,)
    if nro1 == nro2 :
        suma = nro1 + nro2
        print("El suma de ambos números es",suma,) 


           