"""
Suponga que un individuo desea invertir su capital en un banco y desea saber 
cuanto dinero ganara después de un mes si el banco paga a razón de 2% mensual. 
"""

capital = 0
#tasa de interes de un 2% que pasare a decimal -> 2 / 100 -> 0.02
tasa_mensual = 0.0


capital = int(input("Ingrese el monto del capital inicial: "))
tasa = float(input("Ingrese la tasa mensual: "))

tasa = tasa / 100

if capital > 0:
    



ganancia = capital * tasa_mensual

print(f"Al cabo de un mes con una tasa de interes del 2% tendra una ganancia de ${ganancia}.")



"""
