"""
Deben pedir al usuario hasta donde la quiere 
que llegue la serie de números.
Desplegar si el numero es par o impar.
"""
contador = 1
serie = 0

serie = int(input("Ingrese la cantidad de números que tenga la serie: "))

while contador <= serie:
    if contador % 2 == 0:
        print("El número" ,contador,"es par.")
    else: 
        print("El número" ,contador,"es impar.")
    contador = contador + 1
print("Fin")


    

