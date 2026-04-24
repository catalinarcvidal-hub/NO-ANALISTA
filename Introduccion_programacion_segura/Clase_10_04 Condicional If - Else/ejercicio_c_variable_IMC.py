"""
Desarrolle un programa que permita ingresar la estatura 
y peso, si al dividir el peso por la estatura al cuadrado 
el valor es menor a 25 deplegaremos por pantalla peso normal, 
si sobrepasa los 25 mostraremos sobrepeso.

"""

estatura = 0.0
peso = 0.0 
imc = 0

estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso: "))

imc = peso/(estatura*estatura)

if imc < 25 :
    print("Peso normal") 
else: 
    print("Sobrepeso")