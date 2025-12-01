"""
3.crea una matriz M de tamaño NxM, y llenar en la diagonal principal la serie fibonacci:
ej: N = 4
    [ 0 , 0 , 0 , 0 ]
    [ 0 , 1 , 0 , 0 ]
    [ 0 , 0 , 1 , 0 ]
    [ 0 , 0 , 0 , 2 ]
"""
#FUNCIONES:
#creacion de una matriz:
def crearm(m,n):
    x = 0
    for i in range(n):
        for j in range(n):
            if(i==j):
                m[i][j] = fibo(x)
                x = x + 1
#mostrar la matriz:
def mostrarm(m,n):
    for i in range(n):
        for j in range(n):
            print(m[i][j],end="\t")
        print()
#una funcion para la fibonacci
def fibo(n):
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        a = b
        b = c
    return a
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese el tamaño de la matriz cuadrada: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    m = [[0]*n for _ in range(n)]
    crearm(m,n)
    fibo(n)
    print("***matriz creada llenado diagonal principal***")
    mostrarm(m,n)
main()