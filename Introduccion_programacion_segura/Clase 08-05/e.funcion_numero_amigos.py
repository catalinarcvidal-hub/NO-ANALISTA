"""
1. Desarrolle una funcion que reciba dos 
números como argumento y me retorne un true si esos dos números son amigos
(la suma de los divisores del primer numero es igual que del segundo).
"""

def numeros_amigos(a,b):
  suma_a = 0
  suma_b = 0

  for x in range(1,a):
    if a % x == 0:
      suma_a = suma_a + x

  for x in range(1,b):
    if b % x == 0:
      suma_b = suma_b + x

  if suma_a == b and suma_b == a:
    return True
  else:
    return False
    

print(numeros_amigos(284,220))




  
      



  
  
  
