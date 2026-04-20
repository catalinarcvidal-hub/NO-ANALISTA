"""
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea 
saber cuanto deberá pagar finalmente por su compra.
"""
descuento = 0
precio = 0

precio = int(input("Ingrese el valor del producto: "))
descuento = int(input("Ingrese el porcentaje de descuento (Sin el signo %): "))

#Calculo para convertir el descuento en decimal.
descuento = descuento / 100
#Calculo para restarle al precio original el descuento.
precio_final = precio - (precio * descuento)

print(f"El total a pagar es de ${precio_final}")
