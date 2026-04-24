"""
Desarrolle un programa que permita ingresar un número, si es
negativo debemos enviar un mensaje al usuario, "Número inválido, 
reingrese" y debe volver a ingresar otro número, si es positivo 
enviamos un mensaje "Número correcto" y termina el programa.

"""
num = 0
num2 = 0

num = int(input("Ingrese un número: "))

if num > 0 :
    print ("Número correcto.")
else : 
    print ("Número inválido, reingrese.")
    num = int(input("Ingrese un numero igual o mayor a 0: "))
if num > 0 :
    print ("Número correcto.")
else : 
    print ("Número inválido, reingrese.")