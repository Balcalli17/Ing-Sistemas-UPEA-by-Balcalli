"""
1.generamos una matriz M de tamaño NxM:
[ 1  , 2  , 3  , 4  ]
[ 5  , 6  , 7  , 8  ]
[ 9  , 10 , 11 , 12 ]
[ 13 , 14 , 15 , 16 ] 
"""
#FUNCIONES:
def generar_matriz(m,n): #creamos una funcion para generar una matriz con la condicion.
    c = 1
    for i in range(n): 
        for j in range(n):
            m[i][j]=c
            c += 1
def muestra_matriz(m,n): #creamos una matriz para mostrar en pantalla en la matriz
    for i in range(n):
        for j in range(n):
            print("%5d" % (m[i][j]),end="")
        print("")
#PRINCIPAL:
def main():
#generar la matriz M
#lectura del tamaño de la matriz
    n = int(input("tamaño de la matriz: "))
#declarar la matriz
    m = [[0]*n for i in range(n)]
#vamos a ver el cuerpo del programa
    generar_matriz(m,n)
    muestra_matriz(m,n)
main()