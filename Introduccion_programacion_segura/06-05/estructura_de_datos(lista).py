"""
Listas son estructuras de datos (Diccionario, vectores, matrices, etc) que nos permiten guardar bajo un nombre especifico muchos elementos.
Ej. Ingresar 10 numeros y luego de ingresarlos saber cual es mayor al ultimo numero ingresado.

dinamicas/mutables : Nos permite crecer o disminuir elementos ( lista )
estatica/inmutables: Se establece una cantidad de elementos que no se pueden agregar ni restar.

Indice: empieza del 0 al numero que se requiera y cada numero se guarda un elemento que nosotros queramos.

para saber lo que hay en el indice ponemos A[1] lo que esta entre corchetes es el indice y el A es el nombre de la estructura de datos "lista"



Para recorrer la lista completa
"""
#          0  1  2  3  4
numeros = [2, 5, 1, 4, 7]

print(f"Elemento índice 2 -> {numeros[2]}")

#Recorrer lista con ciclo for
# num es la variable que guarda el elemento.
for num in numeros:
   print(num)

# funcion len entrega cuantos elementos son.
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
#Métodos de una lista
edades = []
edades.append(48)
edades.append(27)
edades.append(26)
edades.append(28)
edades.append(29)
edades.append(30)
print(edades)
# Metodo insert es para agregar, se pone primero el indice donde queremos que se inserte se separa por una coma y luego se pone el elemento a añadir.
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
elemento_cero = edades.pop(0)
print("Se eliminó el elemento del índice cero, su valor era -> ", elemento_cero)
print(edades)
#Modificar un elemento
edades[2] = 1
print(edades)

#Es complicado hacer metodos en listas estaticas.

#Metodo para insertar un elemento 
edades.insert()

"""
INVESTIGAR

Vectores, arreglos, matrices.

Respuesta en word "Formas de organizar datos"

"""