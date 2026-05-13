"""
Desarrollar una función para detectar numeros perfectos que . es_perfecto(numero).
"""

#El argumento no lo debo incializar, ya que este dato se entrega al llamar a la función en este caso, en el print final.

def es_perfecto(numero):
    suma_divisores = 0

    for i in range(1,numero-1):
        if numero % i == 0:
            suma_divisores = suma_divisores + i

    if numero == suma_divisores:
        return True
    else:
        return False


print(es_perfecto(27))

#Hacer funcion para mostrar los primeros 5 numeros perfectos.

def contar_numeros_perfectos(cuantos):
    suma_perfectos = 0
    n = 1

    while suma_perfectos <= cuantos:
        if es_perfecto()



"""
realizacion del profe
                        
def primeros_perfectos(n: int):
   mis_perfectos = []
   numero = 1
   cont = 1
   while cont <= 5:
      print(numero) #Esto es solo para ver si el contador esta trabajando.
      if es_perfecto(numero):
         mis_perfectos.append(numero)
         cont = cont + 1

      numero = numero + 1

   return mis_perfectos

   **Nunca una funcion debe incluir input o print.**
   **Para lo que se viene investigar Json, que es universal para convertir lo que sea o que distintos lenguajes se entienda***
   
"""
        



