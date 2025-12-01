"""
5.generar la matriz M de tamaño NxM, buscar el 1er numero par en la primera fila y colocar "1"
en su columna:
ej: N = 4
-------------matriz creada:-------------------
        [ 7  ,  [6] , 1  ,  2 ]
        [ 3  ,  10  , 1  ,  0 ]
        [ 4  ,  25  , 3  ,  7 ]
        [ 12 ,   6  , 9  ,  4 ]
----------------------------------------------

        de la 1ra fila el [6] es par,
        aplicamos la condicion...

-------------nueva matriz:--------------------
        [ 7  ,  1  ,  1  ,  2 ]
        [ 3  ,  1  ,  1  ,  0 ]
        [ 4  ,  1  ,  3  ,  7 ]
        [ 12 ,  1  ,  9  ,  4 ]
----------------------------------------------
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

#un procedimiento para la condicion...
def condicionm(m,n):
    i = 0
    sw = 0
    while(i<=n-1 and sw == 0):
        if m[0][i] % 2 == 0:
            sw = 1
        else:
            i = i + 1
    if sw == 0:
        print("en la 1ra fila no existe numeros pares...")
    else:
        for j in range(0,n,1):
            m[j][i]=1

#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese el tamaño de la matriz cuadrada: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    m = [[0]*n for _ in range(n)]
    print("***ingrese los valores de la matriz:***")
    crearm(m,n)
    print("***matriz cuadratica creada:***")
    mostrarm(m,n)
    condicionm(m,n)
    print("***nueva matriz:***")
    mostrarm(m,n)
main()
"""
def condicionm(m,n):
    sw = 0
    for j in range(n):
        if m[0][j]%2==0:
            for i in range(n):
                m[i][j]=1
        else:
            print("no hay pares")

#yo diria que estaria bien en una parte, pero hay que analizar... 
"""