"""
7.crear la matriz M de tamaño MxN en forma de una "G":
    [ 1 , 1 , 1 , 1 , 1 ]
    [ 1 , 0 , 0 , 0 , 0 ]
    [ 1 , 0 , 1 , 1 , 1 ]
    [ 1 , 0 , 0 , 0 , 1 ]
    [ 1 , 1 , 1 , 1 , 1 ]
"""
#FUNCIONES:
#creacion de una matriz:
def crearm(m,n):
    for i in range(n):
        for j in range(n):
            m[i][0]=1
            m[0][j]=1
            m[n-1][j]=1
            m[i//2][n-1]=1
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
    print("***matriz creada:***")
    mostrarm(m,n)
main()