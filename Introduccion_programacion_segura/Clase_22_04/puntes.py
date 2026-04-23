"""
La regla de oro del sep
Para que el sep funcione, los elementos deben estar pasados como argumentos independientes (separados por comas fuera de las comillas).

Si tú escribes esto:
print("Hola Luis", sep="-")
No pasará nada, porque para Python ahí solo hay un gran texto. No tiene nada que separar.

Pero si escribes esto:
print("Hola", "Luis", sep="-")
Resultado: Hola-Luis (Aquí sí hay dos elementos y el sep entra en acción).

El ejemplo con end="" (Vacío)
Este se usa cuando quieres "armar" una palabra o una cifra parte por parte, sin que se note que usaste varios print. No deja ningún espacio ni nada entremedio.

Python
print("C", end="")
print("h", end="")
print("i", end="")
print("l", end="")
print("e", end="")
Resultado en pantalla:
Chile

¿Qué pasó aquí? Al poner las comillas vacías, le prohibiste a Python hacer cualquier espacio o salto. Todo quedó pegado.


Funcion.

str = Para convertir un número a texto.
int = Para convertir texto a número entero.
float =  Para convertir texto a numero decimal.

"""