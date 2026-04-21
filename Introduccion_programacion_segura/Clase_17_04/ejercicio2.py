 
# contador es como dice su nombre el que contará hasta el número 

# que ingreso el usuario.  

contador = 1 

# número se refiere a la caja donde se guardará hasta donde el usuario 

# quiera llegar en la secuencia numérica. 

numero = 0 

#Segundo contador para hacer la secuencia de números desde 1. 

contador2 = 1 

 

print("Te mostrare una secuencia numérica muy entretenida, ¿Hasta qué número quieres llegar?") 

numero = int(input("Ingrese un número: ")) 

 

while contador <= numero: 
    print(contador, end= " ") 
    contador2 = 1 
    while contador2 <= contador: 
        print(contador2, end=" ") 
        contador2 = contador2 + 1 
    contador = contador + 1 
    print() 
print ("Fin") 





