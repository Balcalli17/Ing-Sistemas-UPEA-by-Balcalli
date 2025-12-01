# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es positivo, negativo o cero
if numero > 0:
    signo = "positivo"
elif numero < 0:
    signo = "negativo"
else:
    signo = "cero"

# Verificar si el número es par o impar (solo si no es cero)
if numero != 0:
    if numero % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
else:
    paridad = "no aplica (cero no es par ni impar)"

# Mostrar el resultado
print(f"El número {numero} es {signo} y es {paridad}.")