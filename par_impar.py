# Solicitamos al usuario que ingrese un número entero
n = int(input('Ingrese un numero entero: '))

# Validación de entrada, forma "pura" de validación
# Comprobamos si el número es divisible por 2 (n%2 == 0)
if n % 2 == 0:
    # Si es divisible por 2, el número es par
    print(f'{n} es un número par.')
else:
    # Si no es divisible por 2, el número es impar
    print(f'{n} es un número impar.')

# Forma medio simplificada de determinar si un número es par o impar
# Utilizamos una expresión condicional (if-else) para asignar el valor de la variable 'Salida'
Salida = "Es Par" if n % 2 == 0 else "Es impar"

# Imprimimos el resultado utilizando la variable 'Salida'
print(f'{n} es {Salida}.')

# Forma super simplificada de determinar si un número es par o impar
# Utilizamos una expresión condicional (if-else) para imprimir directamente el resultado
print("Es par" if n % 2 == 0 else "Es impar")

# Comprobamos si el número es positivo, negativo o cero
if n > 0:
    # Si el número es positivo, comprobamos si es par o impar
    print("Es par positivo" if n % 2 == 0 else "Es impar positivo")
elif n < 0:
    # Si el número es negativo, comprobamos si es par o impar
    print("Es par negativo" if n % 2 == 0 else "Es impar negativo")
else:
    # Si el número es cero, lo indicamos
    print('El numero es cero')