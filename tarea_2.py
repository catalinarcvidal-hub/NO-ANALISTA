# Una distribuidora de insumos computacionales compro 20 cajas de mouse. Si cada caja contiene 16 mouse y el valor de cada mouse es de $3500. Cuánto debió cancelar la distribuidora por dicha compra.

#Variables

cant_cajas = 0
mouse_por_caja = 0
valor_por_mouse = 0
total = 0

#Entrada
cant_cajas = int(input("Ingrese la cantidad de cajas compradas: "))
mouse_por_caja = int(input("Ingrese la cantidad de mouse por caja: "))
valor_por_mouse = int(input("Ingrese el valor del mouse por unidad: "))

total = cant_cajas * mouse_por_caja * valor_por_mouse

#Salida
print("Se compraron",cant_cajas,"cajas de mouse en la cual habían",mouse_por_caja,"unidades por caja y cada uno tuvo un valor de",valor_por_mouse,"pesos, con esta información podemos calcular que la distribuidora cancelo",total,"pesos por el pedido completo.")


