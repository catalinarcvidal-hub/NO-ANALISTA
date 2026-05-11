"""
1. Desarrolle una funcion que reciba dos 
números como argumento y me retorne un true si esos dos números son amigos
(la suma de los divisores del primer numero es igual que del segundo).
"""
numero_amigos = 0
a = 0
b = 0

def numeros_amigos(a,b):
  a = 0
  b = 0
  suma = 0

  for x in range(1,a):
    if a % x == 0:
      suma_a = suma_a + x

  for x in range(1,b):
    if b % x == 0:
      suma_b = suma_b + x

  if suma_a == b and suma_b == a:
    print(f"{a} y {b} son números amigos.")


  
      



  
  
  
