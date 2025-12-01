"""
8.crea una matriz M de tamaño MxN y ordenar la matriz de forma ascendente.
ej: N = 4
-matriz creada por el usuario: (claro, el usuario es libre para colocar los numeros que deseen)
    [ 16 , 15 , 14 , 13 ]
    [ 12 , 11 , 10 , 9  ]
    [ 8  , 7  , 6  , 5  ]
    [ 4  , 3  , 2  , 1  ]
-matriz ordenada ascendentemente:
    [ 1  , 2  , 3  , 4  ]
    [ 5  , 6  , 7  , 8  ]
    [ 9  , 10 , 11 , 12 ]
    [ 13 , 14 , 15 , 16 ]
"""
#FUNCIONES:
#creacion de una matriz:
def crearm(m,n):
    for i in range(n):
        for j in range(n):
            m[i][j]=int(input(f"m[{i}][{j}]="))
            
#mostrar la matriz:
def mostrarm(m,n):
    for i in range(n):
        for j in range(n):
            print(m[i][j],end="\t")
        print()
#ordenar la matriz:
def ordenarm(m,v,n):
    k = 0
    for i in range(n):
        for j in range(n):
            v[k] = m[i][j]
            k = k + 1
    for i in range(1,k,1):
        for j in range(0,k-1,1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
    l = 0
    for i in range(n):
        for j in range(n):
            m[i][j] = v[l]
            l = l + 1
#PRINCIPAL:
def main():
    while(True):
        n = int(input("ingrese el tamaño de la matriz cuadratica: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    m = [[0]*n for _ in range(n)]
    v = [0]*(n*n)
    print("ingrese los valores de una matriz:")
    crearm(m,n)
    print("matriz original:")
    mostrarm(m,n)
    ordenarm(m,v,n)
    print("matriz ordenada:")
    mostrarm(m,n)
main()
    