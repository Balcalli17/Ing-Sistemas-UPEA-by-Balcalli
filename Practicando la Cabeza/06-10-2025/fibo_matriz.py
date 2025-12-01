"""
1.generamos una matriz FIB de tamaño NxM:
[ 0   , 1   , 1   , 2   ]
[ 3   , 5   , 8   , 13  ]
[ 21  , 34  , 55  , 89  ]
[ 144 , 233 , 377 , 610 ] 
"""
#FUNCIONES:
def crearm(m,n):
    a = 0
    b = 1
    for i in range(n): 
        for j in range(n):
            c = a + b
            m[i][j] = a
            a = b
            b = c
def mostrarm(m,n):
    for i in range(n):
        for j in range(n):
            print("%5d" % (m[i][j]),end="")
        print("")
#PRINCIPAL:
def main():
    while(True):
        n = int(input("ingrese el tamaño de la matriz cuadrada: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    a = 0
    b = 1
    m = [[0]*n for _ in range(n)]
    crearm(m,n)
    mostrarm(m,n)
main()