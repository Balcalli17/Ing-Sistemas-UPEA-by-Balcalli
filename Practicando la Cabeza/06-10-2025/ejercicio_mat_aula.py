"""
1.generamos una matriz MAT de tamaño NxM:
[ 16 , 15 , 14 , 13 ]
[ 12 , 11 , 10 , 9  ]
[ 8  , 7  , 6  , 5  ]
[ 4  , 3  , 2  , 1  ] 
"""
#FUNCIONES:
def generar_matriz(m,n):
    c = 1
    for i in range(n-1,-1,-1): 
        for j in range(n-1,-1,-1):
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
            