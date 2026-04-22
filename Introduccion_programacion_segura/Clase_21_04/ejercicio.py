"""
Desarrolle un programa que permita ingresar diez números y al finalizar despliegue cual es el myor de ellos.

"""

numero = 0
contador = 1
mayor = 0
primer_numero = True

print("Le pediremos 10 números y al finalizar, desplegaremos el mayor de ellos.")

while contador <= 10:
    print(f"{contador} de 10.")
    numero = int(input("Ingrese un número:  "))
    
    # Al poner una variable booleana (Verdadero o falso) obliga a que el codigo se ejecute ingresando al if, ya que el if busca siempre el verdadero.
    if primer_numero:
        mayor = numero
        #al pasar la linea de codigo el programa podemos ir cambiando lo que contiene las variables pasadas, ahora cambiamos el valor de la variable para que al volver a ejecutar el codigo, no entre mas al if ya que ahora sera falso siempre.
        primer_numero = False
    else:
        if numero > mayor:
            mayor = numero

    contador = contador + 1
print(f"El numero mayor es {mayor}")

    
    