"""
Desarrolle un programa que permita ingresar 3 números y desplegarlos de forma descendente. 
"""

n1 = 0
n2 = 0
n3 = 0
menor = 0
medio = 0
mayor = 0

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese otro número: "))
n3 = int(input("Ingrese un número mas: "))

if n1 < n2 : 
  menor = n1
  if n1 < n3 :
    menor = n1
    if n2 < n3:
      medio = n2
      mayor = n3
    else: 
      medio = n3
      mayor = n2
else :
  if n2 < n3:
    menor = n2
    if n1 < n3:
      medio = n1
      mayor = n3
    else:
      medio = n3
      mayor = n1
  else: 
    if n3 < n2: 
      menor = n3
      if n2 < n1:
        medio = n2
        mayor = n1
      else: 
        medio = n1
        mayor = n2

print(f"Los números ingresados serán desplegados en orden descendente: {mayor}, {medio}, {menor}.")