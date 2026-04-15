"""
Generar un programa que determine el rango etareo.
 
0  - 10 -> Infante
11 - 18 -> Preadolescente
18 - 30 -> Adulto joven
30 - 50 -> Adulto
50 - +  -> Adulto mayor

"""
edad = 0

edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad <= 130:
    if edad >= 0 and edad <= 10:
        print("Usted esta en el rango de edad de infante")
    if edad >= 11 and edad <= 18:
        print("Usted se encuentra en el rango de edad de preadolescente")
    if edad >= 18 and edad <= 30:
        print("Usted se encuentra en el rango de edad de adulto joven")
    if edad >= 30 and edad <= 50:
        print("Usted se encuentra en el rango de edad de adulto")
    if edad >= 50 :
        print("Usted se encuentra en el rango de edad de adulto mayor")
else: 
    print ("Edad invalida, su edad debe estar entre 0 y 130 años")