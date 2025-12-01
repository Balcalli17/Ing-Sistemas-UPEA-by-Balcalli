"""
13.Realiza un programa para leer un número n entero positivo y la función 
para hallar la suma de los factoriales de los dígitos menores a 5.
ej: ENTRADA: ingrese n: 26534 , SALIDA: suma= 4! + 3! + 2! , suma factorial: 32
"""
#FUNCIONES:
def sum_fact_5(num):
    s = 0
    while(num > 0):
        d = num % 10
        if d < 5:
            fact=1
            for i in range(1,d+1):
                fact = fact * i
            s = s + fact
        else:
            num = num // 10
        num = num // 10
    return s
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese valor de n entero positivo: "))
        if n > 0:
            break
    res = sum_fact_5(n)
    print(res)
main()