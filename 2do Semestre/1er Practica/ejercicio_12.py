"""
12.Realiza una función que reciba un numero entero y retorne la multiplicación de sus dígitos pares.
ej:ENTRADA: 24235 , SALIDA: la multiplicacion de los pares son: 16
"""
#FUNCIONES:
def par_multi(num):
    m = 1
    while(num > 0):
        d = num % 10
        if d == 0:
            num = num // 10
        else:
            if d % 2 == 0:
                m = m * d
            else:
                d = 0
            num = num // 10
    return m
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese un numero entero positivo: "))
        if n > 0:
            break
    
    res = par_multi(n)
    print(res)
main()
