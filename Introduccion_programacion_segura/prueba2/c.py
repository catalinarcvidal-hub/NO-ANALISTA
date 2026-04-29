"""
Un teatro otorga descuentos según la edad del cliente. Determinar la cantidad de dinero que el teatro deja de percibir por cada 
una de las categorías. Tomar en cuenta que los niños menores de 5 años no pueden entrar al teatro y que existe un precio único
($ 10.000.-) en los asientos. 

Los descuentos se hacen tomando en cuenta el siguiente cuadro: 
Categorías Edad Descuento 
Categoría 1 -> 5 - 14 -> 35 % 
Categoría 2 -> 15 - 19 -> 25 % 
Categoría 3 -> 20 - 60 -> 0 %
Categoría 4 -> Mayor de 60 años -> 90% 

Desarrolle un programa que permita ingresar la cantidad de personas que pueden entrar al teatro, luego por cada entrada calcular 
según edad del cliente.
Al finalizar el último cliente entregar el siguiente detalle:

a) Total recaudado.
b) Cantidad de clientes ingresada ingresados en cada categoría.
c) Total de descuentos aplicados.

"""

capacidad = 0
contador = 1

precio_unico = 10000
precio_actual = 0
edad = 0
descuento = 0.0

recaudacion = 0
recaudacion_categoria_uno = 0
recaudacion_categoria_dos = 0
recaudacion_categoria_tres = 0
recaudacion_categoria_cuatro = 0

total_descuentos = 0
total_dcto_categoria_uno = 0
total_dcto_categoria_dos = 0
total_dcto_categoria_tres = 0
total_dcto_categoria_cuatro = 0

total_asistentes_categoria_uno = 0
total_asistentes_categoria_dos = 0
total_asistentes_categoria_tres = 0
total_asistentes_categoria_cuatro = 0

capacidad = int(input("Ingrese la capacidad de personas que tiene el teatro: "))

while contador <= capacidad:
    print(f"{contador} de {capacidad}.")
    edad = int(input("Ingrese la edad del asistente: "))

    if edad < 5:
        print("Los niños menores a 5 años no pueden ingresar.")
        
    else:
        if edad >= 5 and edad <= 14:
            descuento = 0.35
            

            descuento = precio_unico * descuento #3.500 de descuento
            total_dcto_categoria_uno = total_dcto_categoria_uno + descuento

            precio_actual = precio_unico - descuento #6.500 precio actual
            recaudacion_categoria_uno = recaudacion_categoria_uno + precio_actual

            total_asistentes_categoria_uno = total_asistentes_categoria_uno + 1

            contador = contador + 1

        #Categoría 2 -> 15 - 19 -> 25 % 
        if edad >= 15 and edad <= 19:
            descuento = 0.25
            
            descuento = precio_unico * descuento # 2.500 de dcto
            total_dcto_categoria_dos= total_dcto_categoria_dos + descuento

            precio_actual = precio_unico - descuento # 7.500 precio actual
            recaudacion_categoria_dos = recaudacion_categoria_dos + precio_actual

            total_asistentes_categoria_dos = total_asistentes_categoria_dos + 1

            contador = contador + 1

        #Categoría 3 -> 20 - 60 -> 0 %
        if edad >= 20 and edad <= 60:
            descuento = 0
            
            descuento = precio_unico * descuento # 0 de dcto
            total_dcto_categoria_tres= total_dcto_categoria_tres + descuento

            precio_actual = precio_unico - descuento # 10.000 precio actual
            recaudacion_categoria_tres = recaudacion_categoria_tres + precio_actual

            total_asistentes_categoria_tres = total_asistentes_categoria_tres + 1

            contador = contador + 1

        #Categoría 4 -> Mayor de 60 años -> 90%
        if edad > 60:
            descuento = 0.90
            
            descuento = precio_unico * descuento # 9.000 de dcto
            total_dcto_categoria_cuatro = total_dcto_categoria_cuatro + descuento

            precio_actual = precio_unico - descuento # 1.000 precio actual
            recaudacion_categoria_cuatro = recaudacion_categoria_cuatro + precio_actual

            total_asistentes_categoria_cuatro = total_asistentes_categoria_cuatro + 1

            contador = contador + 1

    

recaudacion = recaudacion_categoria_uno + recaudacion_categoria_dos + recaudacion_categoria_tres + recaudacion_categoria_cuatro
total_descuentos = total_dcto_categoria_uno + total_dcto_categoria_dos + total_dcto_categoria_tres + total_dcto_categoria_cuatro
print()
print(f"En la categoria 1 que son las personas de 5 a 14 años ingresaron {total_asistentes_categoria_uno}.")
print(f"En la categoria 2 que son las personas de 15 a 19 años ingresaron {total_asistentes_categoria_dos}.")
print(f"En la categoria 3 que son las personas de 20 a 60 años ingresaron {total_asistentes_categoria_tres}.")
print(f"En la categoria 4 que son las personas de 60 años o mas ingresaron {total_asistentes_categoria_cuatro}.")
print()
print(f"El total recaudado fue de ${recaudacion}")
print()
print(f"El total de los descuentos fue de ${total_descuentos}")



