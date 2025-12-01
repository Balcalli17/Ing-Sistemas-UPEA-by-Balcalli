"""
1.generamos una matriz M de tamaño NxM:
[ 1  , 5  , 8  , 10 ]
[ 2  , 6  , 9  , 0  ]
[ 3  , 7  , 0  , 0  ]
[ 4  , 0  , 0  , 0  ] 
"""
#FUNCIONES:
def generar_matriz(m,n):
    c = 1
    for i in range(0,n,1): 
        for j in range(0,n,1):
            m[j][i]=c
            c = c + 1
        n = n - 1
def muestra_matriz(m,n):
    for i in range(n):
        for j in range(n):
            print("%5d" % (m[i][j]),end="")
        print("")
#PRINCIPAL:
def main():
    while(True):
        n = int(input("ingrese tamaño de la matriz cuadrada: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    mat = [[0]*n for _ in range(n)]
    generar_matriz(mat,n)
    muestra_matriz(mat,n)
main()