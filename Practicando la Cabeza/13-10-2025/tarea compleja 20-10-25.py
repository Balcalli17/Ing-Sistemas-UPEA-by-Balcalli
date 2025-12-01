"""
Dado un vector V de tamaño N (Multiplo de 3)
1. Hallar la suma de cada parte y verificar si es primo, y ordenar de forma ascendentemente.
ej: N=9
    V = [ 7 , 2 , 1 , 15 , 11 , 8 , 14 , 3 , 20 ]
        |    10     |     34      |      37     |
                                      es primo
                                    (ascendente)

2.si la suma no es primo, verificar si es parte de fibonacci ordenar descendente.
3.si un cumple el (1.) ni el (2.), ordenar solo los pares.
"""
#FUNCIONES:
def crearv(v,n):
    for i in range(0,n,1):
        v[i] = int(input(f"[{i}]="))

def mostrarv(v,n):
    for i in range(n):
        print(v[i],end="-")
    print()

def ordenar(v,n):
    sum=0
    sum2=0
    sum3=0
    t = n // 3
    t2 = t * 2
    for i in range(0,t,1):
        sum = sum + v[i]
    print("1er parte:",sum)
    if es_primo(sum) == True:
        print("es primo")
    else:
        print("no es primo")
    for i in range(t,t2,1):
        sum2 = sum2 + v[i]
    print("2da parte:",sum2)
    if es_primo(sum2) == True:
        print("es primo")
    else:
        print("no es primo")
    for i in range(t2,n,1):
        sum3 = sum3 + v[i]
    print("3ra parte:",sum3)
    if es_primo(sum3) == True:
        print("es primo")
    else:
        print("no es primo")

def es_primo(n):
    if n < 2:
        return False
    divisor = 1
    contador = 0
    while divisor <= n:
        if n % divisor == 0:
            contador = contador + 1
        divisor = divisor + 1
    if contador == 2:
        return True
    else:
        return False
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese el tamaño del vector (solo numeros multiplo de 3): "))
        if n > 0:
            break
        else:
            print("ingrese un numero multiplo de 3...")
    v=[0]*n
    print("ingrese los valores del vector:")
    crearv(v,n)
    print("***vector creado:***")
    mostrarv(v,n)
    ordenar(v,n)
    
main()