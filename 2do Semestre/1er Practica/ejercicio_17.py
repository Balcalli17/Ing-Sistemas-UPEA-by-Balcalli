"""
17.Realiza una función que reciba un numero positivo y de cada digito 
mostrar su factorial y luego mostrar la sumatoria de los factoriales.
ej: ENTRADA: Introduzca un número n=1235 ,SALIDA: 120,6,2,1 suma=129
"""
#FUNCIONES:
def desc_fact(num):
    s = 0
    while(num > 0):
        d = num % 10
        fact = 1
        for i in range(1,d+1):
            fact = fact * i
        print(fact,end=",")
        s = s + fact
        num = num // 10
    return s

#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese valor de n entero positivo: "))
        if n > 0:
            break
    res = desc_fact(n)
    print("")
    print(f"la suma de los factoriales es: {res}")
main()