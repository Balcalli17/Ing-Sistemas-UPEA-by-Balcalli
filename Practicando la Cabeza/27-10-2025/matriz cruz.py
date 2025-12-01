"""
crea la siguiente matriz:
ej: N = 5
    [ 0 , 0 , 1 , 0 , 0 ]
    [ 0 , 0 , 1 , 0 , 0 ]
    [ 1 , 1 , 1 , 1 , 1 ]
    [ 0 , 0 , 1 , 0 , 0 ]
    [ 0 , 0 , 1 , 0 , 0 ]

    N = 6
    [ 0 , 0 , 1 , 1 , 0 , 0 ]
    [ 0 , 0 , 1 , 1 , 0 , 0 ]
    [ 1 , 1 , 1 , 1 , 1 , 1 ]
    [ 1 , 1 , 1 , 1 , 1 , 1 ]
    [ 0 , 0 , 1 , 1 , 0 , 0 ]
    [ 0 , 0 , 1 , 1 , 0 , 0 ]
"""
#FUNCIONES:
def crearm(m,n):
    mat = n // 2
    for i in range(n):
        m[i][mat] = 1
        m[mat][i] = 1
    if n%2 == 0:
        for i in range(n):
            m[i][mat-1]=1
            m[mat-1][i]=1
    
def mostrarm(m,n):
    for i in range(n):
        for j in range(n):
            print(m[i][j],end="\t")
        print("")

#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese tamaño de la matriz cuadrada: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    m = [[0]*n for _ in range(n)]
    crearm(m,n)
    mostrarm(m,n)
main()