"""
14.Realiza un programa para leer un número n entero positivo y la función 
hallar la suma de los factoriales de los dígitos múltiplos de 3.
ej: ENTRADA: ingrese n: 26534 ,SALIDA: suma: 6! + 3! , suma = 726
"""
#FUNCIONES:
def sum_fact_mult_3(num):
    s = 0
    while(num > 0):
        d = num % 10
        if d % 3 == 0:
            fact=1
            for i in range(1,d+1):
                fact = fact * i
            s = s + fact
        num = num // 10
    return s
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese valor de n entero positivo: "))
        if n > 0:
            break
    res = sum_fact_mult_3(n)
    print(res)
main()