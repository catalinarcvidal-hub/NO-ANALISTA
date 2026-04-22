'''C)	Desarrolle un programa que permita ingresar 3 notas y al finalizar despliegue el promedio.'''

n1 = 0
n2 = 0
n3 = 0
pro = 0

n1 = float(input("Ing. 1ra nota :"))
n2 = float(input("Ing. 2da nota :"))
n3 = float(input("Ing. 3ra nota :"))

pro = (n1 + n2 + n3) / 3

print(f"Promedio {pro}")

if pro >= 4 :
    print("Aprobado")
else :
    print("Reprobado")

print("Espero que el resultado haya sido el esperado! Si no, exito para la próxima<3")
notbooklm