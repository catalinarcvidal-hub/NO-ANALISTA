"""
Operadores lógicos: and. or, not.

xor (averiguar, no esta dentro de lo que aplicaremos)
algebra  booleana (investigar)

Cuando trabajamos con "and" es para las condicioness
en las que ambas deben ser verdaderos para que entregue
un verdadero.

Ejemplo: if n1 > n2 and n1 > n3

   a   | b | a and b
   .v. | v | v
   .v. | f | f
   .f. | v | f
   .f. | f | f

*Estado booleano es solo dos estados. verdadero (1) y falso (0)
Ejemplo: 
“Salgo si tengo dinero Y tiempo”


"Or" es para las condiciones en las que con que solo 
una condicion se cumpla, es decir, sea verdadera, vuelve
todo lo demas verdadero y en caso de que sea todo falso, 
ahi si queda en falso.

Ejemplo: 

   a   | b | a or b
   .v. | v | v
   .v. | f | v
   .f. | v | v
   .f. | f | f

"not" es para cambiar un valor a otro, como si es falso, 
el not lo vuelve verdadero.
Ejemplo:
“Salgo si tengo dinero O me invitan”


| = pipe

   a | not a
   v | f
   f | v

investigar exadecimal   

INVESTIGAR:

xor (No esta dentro de lo que aplicaremos pero para
tener nocion de lo que es)
Algebra  booleana
Sistema exadecimal (cada 16 ciclos)  
Numeros binarios. 
Suma de binarios
Conversion de decimal a binarios e inversa.

"""
"""
#Ejercicio mayor de 3 números.

numA = int(input("1er número : "))
numB = int(input("2do número : "))
numC = int(input("3er número : "))

if numA > numB and numA > numC:
   print(numA)
else:
   if numB > numC:
      print(numB)
   else:
      print(numC)
"""
"""
#Ejercicio de determinar mayor o menor de edad.

edad = int(input("Edad : "))

if edad > 0 and edad < 130:
   if edad <= 18:
      print("mayor")
   else:
      print("menor")
else:
   print("!!!...Edad inválida, debe esta entre cero y 130...!!!")

"""