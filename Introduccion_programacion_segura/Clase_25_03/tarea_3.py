#Una persona tiene $100.000 y decide invertir $70.000 de ellos en bonos hipotecarios a un 5% (mensual) y el resto en un depósito a plazo a un 10% (mensual).  ¿Cuánto dinero ganará esta persona después de n mes?.

#Variables

capital = 100000
monto_inv_bono_hipotecario = 70000
porcentaje_ganancia_mensual_bono = 5

#Con los datos entregados en el ejercicio realice el calculo para sacar la inversion destinada al deposito a plazo.
monto_inv_deposito_a_plazo = (capital - monto_inv_bono_hipotecario)
porcentaje_ganancia_mensual_deposito = 10


#Entrada
#Los datos que le consultare al usuario no es necesa<rio declararlo en las variables.
cantidad_de_meses_de_inv = int(input("Ingrese la cantidad de meses que deseé invertir: "))

#Con estas operaciones puedo volver el porcentaje a decimal y asi calcular mi ganancia.
porcentaje_en_decimal_bono = (porcentaje_ganancia_mensual_bono / 100)
porcentaje_en_decimal_deposito = (porcentaje_ganancia_mensual_deposito / 100)
#Con los datos adquiridos y las siguientes operaciones calculare la ganancia mensual de las inversiones.
ganancia_de_bono_hipotecario_por_mes = (monto_inv_bono_hipotecario * porcentaje_en_decimal_bono)
ganancia_de_deposito_a_plazo_por_mes = (monto_inv_deposito_a_plazo * porcentaje_en_decimal_deposito)

monto_de_ganancia = (cantidad_de_meses_de_inv * ganancia_de_bono_hipotecario_por_mes) + (cantidad_de_meses_de_inv * ganancia_de_deposito_a_plazo_por_mes)

#Salida

print("Esta persona ganara un total de",monto_de_ganancia,"pesos al invertir",cantidad_de_meses_de_inv,"meses." )

