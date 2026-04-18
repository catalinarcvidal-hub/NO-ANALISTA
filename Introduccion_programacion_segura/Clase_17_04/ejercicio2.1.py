"""
......................................................................
\ = AltGr + ? se llama backslash

\n es para que una parte del texto de un print salte a la linea
de codigo de abajo.

Ejemplo:

    print("Hola\nMundo")

    Resultado:

    Hola
    Mundo

.....................................................................

=sep Es para elegir qué aparece entre valores (separador)

Ejemplo:

    print("Pan", "Queso", "Jamón", sep=" - ")

        En este caso hay un espacio entre las comillas y el 
        signo "-" estos espacios se consideran en la salida 
        de texto, si no los tuviera el texto se veria así: 
        Pan-Queso-Jamón

    Resultado:

    Pan - Queso - Jamón

.........................................................................
Usas end= para mostrar un print al lado de otro debido a que
por defecto print hace salto de línea, pero puedes cambiarlo: usando este 

Ejemplo:
        print("Hola", end=" ")
        print("Mundo")

    Salida por pantalla:

        Hola Mundo 
    
    Si no tuviera el end= la salida de texto seria por defecto:

        Hola
        Mundo

..........................................................................

Resumen rápido

\n → salto de línea |  print("Hola\nMundo")   
sep="..." → separador entre valores | print("Pan", "Queso", "Jamón", sep=" - ")
end="..." → qué pasa al final del print | print("Hola", end=" ")

.........................................................................
"""
# contador es como dice su nombre el que contará hasta el número
# que ingreso el usuario. 
contador = 1
# numero se refiere a la caja donde se guardara hasta donde el usuario
# quiera llegar en la secuencia númerica.
numero = 0
# Este segundo contador sera para establecer la secuencia de numeros
# que debe ir al costado del primer digito.
contador2 = 1

print("Te mostrare una secuencia númerica muy entretenida, ¿Hasta que número quieres llegar?")
numero = int(input("Ingrese un número: "))

while contador <= numero:
    print(contador, end=" ") 
    contador = contador + 1
    
