"""
Confeccione un algoritmo en diagrama de flujo que al
leer el neto de una factura, calcule el I.V.A. y de 
cómo salida el total de la 
factura. 
"""
neto = 0
iva = 0.19
total = 0



neto = int(input("Ingrese el precio neto: "))

total = neto + iva

print(f"NETO : {neto}")

iva = neto * iva
print(f"IVA (19%) : {iva}")

total = neto * 1.19
print(f"TOTAL : {total}")













"""
Para calcular el impuesto: Multiplica por 0,19.

Para agregar el impuesto: Multiplica por 1,19.

Para quitar el impuesto: Divide por 1,19.


Es una duda muy común, pero la diferencia es fundamental porque representan cosas distintas: uno es una **parte** y el otro es el **todo más esa parte**.

Aquí te explico la lógica matemática para que no se te olvide nunca:

### 1. El 0,19 representa solo el impuesto
Cuando multiplicas por **0,19**, estás calculando únicamente el **valor del 19%**. Es como si separaras el impuesto en una cajita aparte.
* **Matemáticamente:** $19 / 100 = 0,19$.
* **Resultado:** Solo obtienes el monto del IVA.

### 2. El 1,19 representa el Total (Neto + IVA)
Aquí está el truco. El número **1** representa el **100%** del valor original del producto (el precio base). Cuando multiplicas por **1,19**, estás haciendo una suma abreviada:

$$1,19 = 1,00 (\text{el producto}) + 0,19 (\text{el impuesto})$$

Al multiplicar por **1,19**, le estás diciendo a la calculadora: *"Dame el valor del producto completo más su 19% de una sola vez"*.

---

### Ejemplo comparativo
Imagina que un router cuesta **$10.000**:

* **Si usas 0,19:**
    $10.000 \times 0,19 = \$1.900$
    *(Solo sabes cuánto es el impuesto, pero no el total).*

* **Si usas 1,19:**
    $10.000 \times 1,19 = \$11.900$
    *(Ya tienes el precio final que hay que pagar en caja).*

### En resumen:
* Multiplicar por **0,19** es para **extraer** el dato.
* Multiplicar por **1,19** es para **actualizar** el precio al valor final.

Es como lo que viste con el **3%**: no es lo mismo calcular cuánto es el 3% de una cuenta ($0,03$), que calcular el total de la cuenta con un recargo del 3% ($1,03$).

¿Te queda más clara la diferencia con esta explicación del "1" como el valor base?

"""