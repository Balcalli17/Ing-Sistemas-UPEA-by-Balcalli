"""
4.generar la matriz M de tamaño NxM y llenar la columna central:
ej: N = 4 (si el tamaño de la matriz es par)
        [ 0 , 1 , 1 , 0 ]
        [ 0 , 1 , 1 , 0 ]
        [ 0 , 1 , 1 , 0 ]
        [ 0 , 1 , 1 , 0 ]
ej: N = 3 (si el tamaño de la matriz es impar)
        [ 0 , 1 , 0 ]
        [ 0 , 1 , 0 ]
        [ 0 , 1 , 0 ]
        [ 0 , 1 , 0 ]
"""
#FUNCIONES:
#creacion de una matriz:
def crearm(m,n):
    t = n // 2
    if n % 2 == 0:
        for i in range(n):
            m[i][t] = 1
            m[i][t-1] = 1
    else:
        for i in range(n):
            m[i][t] = 1
#mostrar la matriz:
def mostrarm(m,n):
    for i in range(n):
        for j in range(n):
            print(m[i][j],end="\t")
        print()
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
    print("***matriz creada llenado diagonal principal***")
    mostrarm(m,n)
main()