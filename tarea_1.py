#TAREA: Don Juan Gonzales compra dos packs de cerveza, 6 latas por pack, una marca dorada y la otra baltica, el total de su compra fue 4.500 y el pack de baltica costo 2.100. ¿Cuanto es el costo de cada lata de cerveza dorada y baltica?
#Variable: marca, precio total. Fijo: 2 packs distintos de 6 cervezas.

#Variables

precio_pack_1 = 0
precio_pack_2 = 0
valor_lata_pack1 = 0
valor_lata_pack2 = 0
cant_de_latas_por_pack = 0
cant_de_pack = 0
total_compra = 0


#Entrada
cant_de_pack = int(input("Ingrese la cantidad de packs que compro: "))
cant_de_latas_por_pack = float(input("Ingrese la cantidad de latas que trae cada pack: "))
marca_primer_pack = input("Ingrese la marca del primer pack de cervezas: ")
marca_segundo_pack = input("Ingrese la marca del segundo pack de cervezas: ")
precio_pack_2 = int(input("Ingrese el precio del segundo pack de cervezas: "))           
total_compra = int(input("Ingrese el total de su compra: "))


precio_pack_1 = (total_compra-precio_pack_2)
valor_lata_pack1 = (precio_pack_1 /cant_de_latas_por_pack)
valor_lata_pack2 = (precio_pack_2 /cant_de_latas_por_pack)

#Salida
print("Juan compro",cant_de_pack,"packs de cervezas de",cant_de_latas_por_pack,"latas por pack, el primer pack es de la marca",marca_primer_pack,"y tuvo un valor de",precio_pack_1,"pesos, por lo que, cada lata tiene un costo de",valor_lata_pack1,"pesos, mientras que el segundo pack es de la marca",marca_segundo_pack,"y tuvo un valor de",precio_pack_2,"pesos y cada lata tiene un costo de",valor_lata_pack2,"pesos, ambos packs tuvieron un costo de",total_compra,"pesos.")
