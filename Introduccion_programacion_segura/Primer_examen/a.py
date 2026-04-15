# A)	Don Juanito es muy detallista en todo, sabe que para lavar 1 kilo de ropa necesita 300 gramos de detergente 
# y 100 gramos de suavizante, hoy llegó a su casa y ya no le queda ropa limpia, debe lavar de inmediato los 13 kilos de ropa sucia 
# que tiene ¿Cuántos KILOS de detergente y suavizante necesita?,
# desarrolle un DF despliegue la información requerida para lavar n kilos de ropa.

#Variable 

cantidad_kg_ropa = 0
gr_detergente = 300
gr_suavizante = 100
kg_detergente = 0 
kg_suavizante = 0
gr_en_un_kilo = 1000

#Entrada

cantidad_kg_ropa = float(input("Ingrese la cantidad de kilos que va a lavar: "))

gr_detergente = cantidad_kg_ropa * gr_detergente
gr_suavizante = cantidad_kg_ropa * gr_suavizante

kg_detergente = gr_detergente / gr_en_un_kilo
kg_suavizante = gr_suavizante / gr_en_un_kilo

#Salida
print("Don Juanito lavará",cantidad_kg_ropa,"kilos de ropa, por lo que, necesitara",kg_detergente,"kilos de detergente y ",kg_suavizante, "kilos de suavizante.")
