#TAREA: Don Juan Gonzales compra dos packs de cerveza, 6 latas por pack, una marca dorada
# y la otra baltica, el total de su compra fue 4.500 y el pack de baltica costo 2.100. 
#¿Cuanto es el costo de cada lata de cerveza dorada y baltica?
#Variable: marca, precio total. Fijo: 2 packs distintos de 6 cervezas.

#variable
 
marca_1 = ""
marca_2 = ""
val_1er_pack = 0
val_2do_pack = 0
val_lata_1er_pack = 0
val_lata_2do_pack = 0

total_c = 0

marca_1 = int(input("Ingrese la marca de la 1ra cerveza :"))
marca_2 = int(input("Ingrese la marca de la 2da cerveza :"))
valor_2do_pack = int(input("Ingrese el valor de uno de los pack:"))
total_c = int(input("Ingrese el total de su compra :"))

valor_1er_pack = total_c - valor_2do_pack
valor_lata_1er_pack = valor_1er_pack / 6
valor_lata_2do_pack = valor_1er_pack / 6


print("El valor por lata del 1er pack es :")
print("El valor por lata del 2do pack es :")


