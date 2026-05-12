"""
Llenar la lista solo con números pares hasta llegar al 50
"""

lista= []

for x in range(1,51):
    if x % 2 == 0:
        lista.append(x)

print(lista)

#OOOOOOO MUCHO MAS SENCILLO.


lista_pares = []

for x in range(2,51,2):
  lista_pares.append(x)
  
print(lista_pares)
