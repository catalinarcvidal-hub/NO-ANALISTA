"""
CAMBIAR ESTE CODIGO QUE ES UN RELOJ DE WHILE A FOR.

import time

x = 0
while x <= 23:
   y = 0
   while y <= 59:
      z = 0
      while z <= 59:
         print(x, ":", y, ":", z)
         time.sleep(0.2)
         z = z + 1
      y = y + 1
   x = x + 1
print("Fin")

"""
import time

for h in range(0, 24, 1):
    for m in range(0,60,1):
        for s in range(0,60,1):
            print (h,m,s, sep= " : ")
            time.sleep(0)
print("Fin")

"""
definiendo while con true hacemos un ciclo infinito
time.sleep es para dar un tiempo de espera.

import time

while True:
   for h in range(0, 24, 1):
      for m in range(0, 60, 1):
         for s in range(0, 60, 1):
            print(h, ":", m, ":", s)
            #time.sleep(0.2)
"""
