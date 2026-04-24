"""

**Apuntes primera clase de Introducción a la programacion.**

FUNCIONES.

PRINT
    Print es la función que permite al usuario ingresar datos desde el teclado.
    Es para mostrar informacion en la pantalla, todo lo que vaya despues de esta palabra se mostrara en la pantalla, 
    considerando que el texto que queremos mostrar esta entre parentisis y comillas al inicio y al final.")

    Ejemplo
    print("Hola mundo")
    print("Tu edad es:", 26)

INPUT
    Input pide datos al usuario desde el teclado, lo que el usuario ingrese se guardara en la variable que hayamos declarado para esto. 
    Todo lo que entra con input() es texto (string), aunque escribas números.     

    edad = input("Ingresa tu edad: ")
    print("Tu edad es:", edad") o print(f"Tu edad es: {edad}")

TIPOS DE DATOS NÚMERICOS.

INT
    "int" Convierte un valor a número entero (sin decimales).

    Ejemplo: 
    edad = int(input("¿Cuántos años tienes? "))
    print(edad + 1)

    
FLOAT
    "float" Convierte un valor a número decimal.

    Ejemplo: 
    precio = float(input("¿Cuánto cuesta? "))
    print(precio * 2)

¿Por que combinarlos?
Porque input siempre devuelve texto, entonces si quieres hacer operaciones matemáticas con el dato que ingresara el usuario
necesitas convertirlo:

"""
