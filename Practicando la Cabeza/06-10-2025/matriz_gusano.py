"""
1.generamos una matriz M de tamaño NxM: (matriz gusano.)
[ 4  , 3  , 2  , 1  ]
[ 5  , 6  , 7  , 8  ]
[ 12 , 11 , 10 , 9  ]
[ 13 , 14 , 15 , 16 ] 
"""
#FUNCIONES:
def generar_matriz(m,n):
    c = 1
    for i in range(0,n,1):
        if (i%2==0):
            for j in range(n-1,-1,-1):
                m[i][j]=c
                c = c + 1
        else:
            for j in range(0,n,1):
                m[i][j]=c
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
