#Ahora aplicamos mas condiciones para establecer un rango de edad, es decir, que no sea valido ingresar 
#numeros negativos o mayores a 130 años de edad.

edad: 0
edad = int(input("Ingrese su edad: "))


if edad >= 18 :         
    print("Cumples con el limite de edad.")
else :  
    print("No cumples con el limite de edad.")