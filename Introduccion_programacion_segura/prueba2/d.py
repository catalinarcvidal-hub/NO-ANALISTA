"""
D.- 
Desarrolle un programa que solicite hasta donde desea la serie el usuario.
El número que ingrese el usuario debe ser mayor a 5.

Ejemplo.
Hasta donde desea la serie: 10
1+2-3+4-5+6-7+8-9+10=7

"""

contador = 1
serie = 0
suma = 0
se_ve_en_pantalla = ""

while serie < 5: 
    serie = int(input("Ingrese hasta donde quiere que llegue la serie: "))
    if serie < 5:
        print("El número ingresado debe ser mayor o igual a 5.")

while contador <= serie:
    if contador == 1 or contador == 2:
            suma = suma + contador
            if contador == 1:
                se_ve_en_pantalla = se_ve_en_pantalla + "1+"
            else:
                se_ve_en_pantalla = se_ve_en_pantalla + "2-"
    else:
        if contador % 2 == 0:
            suma = suma + contador
            if contador == serie:
                se_ve_en_pantalla = se_ve_en_pantalla + str(contador)
            else:
                se_ve_en_pantalla = se_ve_en_pantalla + str(contador) + "-"
        else:
            suma = suma - contador
            if contador == serie:
                se_ve_en_pantalla = se_ve_en_pantalla + str(contador)
            else:
                se_ve_en_pantalla = se_ve_en_pantalla + str(contador) + "+"
    
    contador = contador + 1

print(f"{se_ve_en_pantalla}={suma}")