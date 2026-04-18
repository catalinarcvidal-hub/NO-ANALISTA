
# contador es como dice su nombre el que contará hasta el número
# que ingreso el usuario. 
contador = 1
# numero se refiere a la caja donde se guardara hasta donde el usuario
# quiera llegar en la secuencia númerica.
numero = 0

print("Te mostrare una secuencia númerica muy entretenida, ¿Hasta que número quieres llegar?")
numero = int(input("Ingrese un número: "))

while contador <= numero:
    print(contador)
    contador = contador + 1




