#Declaracion de variable.

anio_de_nacimiento = 0
anio_actual = 0
ed= 0

#Entrada.

anio_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: ")) 

ed = anio_actual - anio_de_nacimiento

#Salida
print("Estamos en el año", anio_actual, "y usted nacio en el año", anio_de_nacimiento, "por lo que usted tiene", ed, "años")