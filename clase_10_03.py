""

Apuntes primera clase de Introducción a la programacion.


Print es para mostrar informacion en la pantalla, todo lo que vaya despues de esta palabra se mostrara en la pantalla, considerando que el texto que queremos mostrar esta entre parentisis y comillas al inicio y al final.")

Ejemplo
print("Hola mundo")
print("Tu edad es:", 26)

Input pide datos al usuario desde el teclado, lo que el usuario ingrese se guardara en la variable que hayamos declarado para esto.       

edad = input("Ingresa tu edad: ")
print("Tu edad es:", edad)

int Convierte un valor a número entero (sin decimales).

edad = int(input("¿Cuántos años tienes? "))
print(edad + 1)

float Convierte un valor a número decimal.
precio = float(input("¿Cuánto cuesta? "))
print(precio * 2)

¿Por que combinarlos?
Porque input siempre devuelve texto, entonces si quieres hacer operaciones matemáticas
necesitas convertirlo:
numero = input("Ingresa un número: ")  # llega como texto "5"
numero = int(numero)                   # ahora es el número 5
print(numero * 2)                      # resultado: 10

""


