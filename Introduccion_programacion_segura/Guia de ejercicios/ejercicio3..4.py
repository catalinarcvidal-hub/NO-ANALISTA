"""
Leer 20 números e imprimir cuantos son  positivos, cuantos negativos y cuantos neutros. 
"""
numero = 0
contador = 1
contador_dos = 0
contador_tres = 0
contador_cuatro = 0

while contador <= 5:
    numero = int(input("Ingrese un número: "))
                 
    if numero >= 1:
        contador_dos = contador_dos + 1
    if numero == 0:
        contador_tres = contador_tres + 1
    if numero < 0:
        contador_cuatro = contador_cuatro + 1

    contador = contador + 1

print(f"Hay {contador_dos} números positivos.")
print(f"Hay {contador_tres} números neutros.")
print(f"Hay {contador_cuatro} números negativos.")
print("")
print("Fin")


