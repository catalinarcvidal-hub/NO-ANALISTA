"""
Programa para determinar si un número es o no par.
"""

# Inicializamos un contador para llevar el registro de cuántos divisores exactos tiene el número
divisibles = 0

# Iniciamos un ciclo que recorre desde 1 hasta el valor de 'numero' inclusive
for x in range(1, numero + 1):
    # Verificamos si el resto de la división (módulo) es cero
    if numero % x == 0:
        # Si es divisible, incrementamos nuestro contador en 1
        divisibles = divisibles + 1

# Un número es primo si y solo si tiene exactamente dos divisores: 1 y él mismo
if divisibles == 2:
    return True  # Es primo
else:
    return False # No es primo