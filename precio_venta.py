"""
Calcular el precio de venta

Dado el valor de venta de un producto, se debe calcular el impuesto general de las ventas 
(IGV) que es del 18%, y apartir de esto, 
determinar el precio de venta final.

Programa en Python que permite al usuario ingresar el valor de venta del producto. Luego, el 
sistema realiza los cálculos necesarios para hallar el IGV y el precio
de venta final.
"""

# Solicitamos al usuario el valor de venta del producto
valor_venta = float(input("Valor de venta del producto: "))

# Calculamos el IGV (18% del valor de venta)
igv = valor_venta * 0.18

# Calculamos el precio de venta final (sumamos el IGV al valor de venta)
precio_venta_final = valor_venta + igv

# Imprimimos el IGV calculado
print(f"El IGV es: {igv}")

# Imprimimos el precio de venta final
print(f"Precio de venta final: {precio_venta_final}")