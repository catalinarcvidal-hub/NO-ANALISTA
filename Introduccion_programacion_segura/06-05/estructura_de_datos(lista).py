"""
Listas son estructuras de datos (Diccionario, vectores, matrices, etc) que nos permiten guardar bajo un nombre especifico muchos elementos.
Ej. Ingresar 10 numeros y luego de ingresarlos saber cual es mayor al ultimo numero ingresado.

dinamicas/mutables : Nos permite crecer o disminuir elementos ( lista )
estatica/inmutables: Se establece una cantidad de elementos que no se pueden agregar ni restar.

Indice: empieza del 0 al numero que se requiera y cada numero se guarda un elemento que nosotros queramos.

para saber lo que hay en el indice ponemos A[1] lo que esta entre corchetes es el indice y el A es el nombre de la estructura de datos, 
en este caso, el nombre de la lista

Para recorrer la lista completa
"""
#          0  1  2  3  4
numeros = [2, 5, 1, 4, 7]

# Indicamos el nombre de la lista y luego el numero del elemento entre corchetes y cerramos todo en un parentesis     
print(f"Elemento índice 2 -> {numeros[2]}")
#Si ponemos el numero -1, python nos mostrara el ultimo elemento de nuestra variable, el penultimo elemento corresponde al -2 y asi sucesivamente.

#Para imprimir sublsitas que es un rango de elementos de la lista como por ej: Quiero que me muestre el indice 0, 1 y 2. 
#Debo indicar que me muestre desde el 0 : 3, siempre debemos poner un indice mas del que queremos ver.
print(numeros[0:3])
#si no se indica el inicio python por defecto entiende que se toma desde el indice 0 y si no se indica el fin, python considerara 
#que debe llegar al ultimo indice de la lista.
print(numeros[:3])

#Recorrer lista con ciclo for
# num es la variable que guarda el elemento.
for num in numeros:
   print(num)

# funcion len entrega cuantos elementos son en la lista.
print("Elementos de la lista ->", len(numeros))

#Recorrer con while
i = 0
while i < len(numeros):
   num = numeros[i]
   if num % 2 == 0:
      print(f"{num} es par y está en el índice {i}")

   print(num)
   i = i + 1
print(numeros)



#Métodos de una lista

edades = []

#append agrega un elemento al final, lo que es una accion(metodo)
edades.append(48)
edades.append(27)
edades.append(26)
edades.append(28)
edades.append(29)
edades.append(30)
print(edades)

# Metodo insert es para agregar, se pone primero el indice donde queremos que se inserte se separa por una coma y luego se 
# pone el elemento a añadir.
#Insertar en el índice 2 el elemento 36
edades.insert(2, 36)
print(edades)

#Elimina elemento 28 de la lista
#edades.remove(28)
#print(edades)

#Elimina el elemento del índice 4
del edades[4]
print(edades)

#El metodo pop elimina un elemento pero guardando su valor en una variable.
# Si no ponemos nada entre parentesis, se eliminara el ultimo elemento de la lista.
elemento_cero = edades.pop(0)
print("Se eliminó el elemento del índice cero, su valor era -> ", elemento_cero)
print(edades)

#Modificar un elemento
edades[2] = 1
print(edades)

#Es complicado hacer metodos en listas estaticas.

###########################################

#Metodo para voltear la lista.
edades.reverse()

#Metodo para eliminar todos los elementos de la lista y asi dejarla vacia.
edades.clear()

#Metodo para extender un lista al final.
edades.extend([51,21,22])
print(edades)

#metodo para sumar listas
edades = [2,2,8,10]
edades2 = [12,15]

edades3 = edades+edades2

print(edades3)

# Para saber si un elemento en especifico esta en lista, usamos in como condicional.
print(12 in edades)
# Aqui preguntamos si 12 esta en la lista "edades". Al ejecutar nos dira False o True segun corresponda.

#Para saber en que indice se encuentra cierto elemento utilizamos index.
print(edades.index(8))
#Al ejecutar nos indicara que el número 8 esta en el indice 1.

#Metodo count es para saber cuantas veces aparece un elemento en la lista.
print(lista.count(2))

#Metodo sort para ordenar los valores de la lista de manera ascendente.
 edades.sort()
print(edades)

#Metodo sort para ordenar los valores de la lista de manera descendente.
 edades.sort(reverse=True)
print(edades)

######################################

"""
INVESTIGAR

Vectores, arreglos, matrices.

Respuesta en word "Formas de organizar datos"

"""
