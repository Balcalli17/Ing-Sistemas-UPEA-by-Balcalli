"""
6.crea una matriz M de tamaño MxN con la forma de una "C":
    [ 1 , 1 , 1 , 1 , 1 ]
    [ 1 , 0 , 0 , 0 , 0 ]
    [ 1 , 0 , 0 , 0 , 0 ]
    [ 1 , 0 , 0 , 0 , 0 ]
    [ 1 , 1 , 1 , 1 , 1 ]
"""
#FUNCIONES:
#creacion de una matriz:
def crearm(m,n):
    for i in range(0,n,1):
            m[i][0]=1
            m[0][i]=1
            m[n-1][i]=1
"""
*igual funciona de esta maneja pero utilizando un "if" (la mas larga):
def crearm(m,n):
    for i in range(n):
        for j in range(n):
            if(i==0 or j==0 or i==n-1):
                m[i][j] = 1
            else:
                m[i][j] = 0

*ahora sin el "if":
def crearm(m,n):
    for i in range(n):
        for j in range(n):
            m[i][0]=1
            m[0][j]=1
            m[n-1][j]=1

*lo que esta habilitado es la forma mas reducida por mi.
"""
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