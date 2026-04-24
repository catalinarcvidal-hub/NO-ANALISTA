"""
Leer 20 números e imprimir cuantos son  positivos, cuantos negativos y cuantos neutros. 
"""
numero = 0
contador = 1
positivo = 0
negativo = 0
neutro = 0
contador2 = 0
contador3 = 0
contador4 = 0

while contador <= 20:
    numero = int(input("Ingrese un número: "))
    if numero > 0:
        numero = positivo
        contador2 = contador2 + 1
    if numero == 0:
        numero = neutro
        contador3 = contador3 + 1
    if numero < 0:
        numero = negativo
        contador4 = contador4 + 1
    contador = contador + 1

print(f"Hay {contador2} números positivos.")
print(f"Hay {contador3} números neutros.")
print(f"Hay {contador4} números negativos.")
print("")
print("Fin")


