"""
1.generamos una matriz M de tamaño NxM: 
[ 4  , 8  , 12 , 16 ]
[ 3  , 7  , 11 , 15 ]
[ 2  , 6  , 10 , 14 ]
[ 1  , 5  , 9  , 13 ] 
"""
#FUNCIONES:
def generar_matriz(m,n):
    c = 1
    for i in range(0,n,1): 
        for j in range(n-1,-1,-1):
            m[j][i]=c
            c = c + 1
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