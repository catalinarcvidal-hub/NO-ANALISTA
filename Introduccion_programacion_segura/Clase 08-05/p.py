"""
programa que identifique numero primos
"""

def es_primo(numero):
   divisibles = 0

   for x in range(1, numero + 1):
      if numero % x == 0:
         divisibles = divisibles + 1

   if divisibles == 2:
      return True
   else:
      return False
   

print(es_primo(5))
















n = int(input("Ing. número :"))

if es_primo(n):
   print("Primo")
else:
   print("No es primo")









   contar_primo = 0
n = 1
while contar_primo <= 10:
   if es_primo(n):
      contar_primo = contar_primo + 1

   n = n + 1
