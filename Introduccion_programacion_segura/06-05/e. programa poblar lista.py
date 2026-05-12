"""
Desarrolle un programa que permita poblar una lista de tamaño 50 (o sea 49 elementos)
"""
numeros = []

#La x es la variable que es el contador y llegara hasta el 49 ya que el numero que se pone en el parentesis es excluyente, no se considera.
for x in range(1,50):
    #Ponemos el nombre de la lista un punto y append para agregar elementos a la lista.
    numeros.append(x)
#Con este print, me mostrara la lista poblada del 1 al 49 consecutivamente.
print(numeros)
    
