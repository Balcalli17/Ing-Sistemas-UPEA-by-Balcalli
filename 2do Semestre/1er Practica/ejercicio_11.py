"""
11.Realiza un programa que lea un número mayor a cero y encuentre la suma de sus dígitos.
Mostrar el resultado obtenido. 
(Emplee mínimamente 2 módulos para encontrar los resultados)
"""
#FUNCIONES:
def suma_dig(num):
    s = 0
    while (num > 0):
        d = num % 10
        s = s + d
        num = num // 10
    return s

#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese un numero entero positivo: "))
        if n > 0:
            break
    sum = suma_dig(n)
    print(f"la suma de los digitos es: {sum}")
main()