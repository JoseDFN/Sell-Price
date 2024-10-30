# Solicitamos al usuario que ingrese el monto de consumo
monto_consumo = float(input("Ingrese el monto de consumo: "))

# Evaluamos el monto de consumo para determinar el descuento aplicable
if monto_consumo > 50 and monto_consumo <= 100:
    descuento = 0.1
elif monto_consumo > 100 and monto_consumo <= 200:
    descuento = 0.2
elif monto_consumo > 200:
    descuento = 0.3
else:
    # Si el monto de consumo es menor o igual a 50, no se aplica descuento
    descuento = 0.0

# Calculamos el monto del descuento
monto_descuento = descuento * monto_consumo

# Calculamos el total a pagar después del descuento
total = monto_consumo - monto_descuento

# Imprimimos un resumen de la cuenta
print("\n Resumen de la cuenta")
print(f'Monto de consumo es igual a {monto_consumo}')
print(f'Descuento aplicado: {descuento*100}%')

# Imprimimos el monto total con descuento
print(f'Monto total con descuento: {total}')
