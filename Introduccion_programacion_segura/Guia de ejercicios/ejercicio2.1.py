"""
Suponga que un individuo desea invertir su capital en un banco y desea saber 
cuanto dinero ganara después de un mes si el banco paga a razón de 2% mensual. 
"""

capital = 0
tasa_mensual = 0.0

tasa_mensual = float(input("Ingrese el porcentaje de la tasa mensual: "))
capital = int(input("Ingrese el monto del capital inicial: "))

if tasa_mensual > 0 and capital > 0:
    #tasa de interes se pasa a decimal ej: 2% -> 2 / 100 -> 0.02
    tasa_mensual = tasa_mensual / 100
    ganancia = capital * tasa_mensual
    total = capital + ganancia
    print(f"Al cabo de un mes con una tasa de interés del {tasa_mensual}% tendra una ganancia de ${ganancia} y un total de ${total}")
else:
    print("El monto del capital y la tasa mensual deben ser mayor a 0.")




