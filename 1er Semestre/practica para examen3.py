#FUNCIONES:
def diagonalP(n):
    matriz = [[0]*n for _ in range(n)]
    for i in range(0,n):
        for j in range(0,n):
            if (i == j):
                matriz[i][j]=1
            else:
                matriz[i][j]=0
    return matriz

def diagonalS(n):
    matriz = [[0]*n for _ in range (n)]
    for i in range(0,n):
        for j in range(0,n):
            if(i+j==n-1):
                matriz[i][j]=1
            else:
                matriz[i][j]=0
    return matriz

def matrizZ(n):
    matriz = [[0]*n for _ in range(n)]
    for i in range (0,n):
        for j in range(0,n):
            if(i==0) or (i+j==n-1) or (i == n-1):
                matriz[i][j]=1
            else:
                matriz[i][j]=0
    return matriz

def matrizZinver(n):
    matriz = [[0]*n for _ in range (n)]
    for i in range(0,n):
        for j in range(0,n):
            if(j == 0) or (i == j) or (j == n-1):
                matriz[i][j]=1
            else:
                matriz[i][j]=0
    return matriz

def imprimirm(matriz,n):
    for i in range(0,n):
        for j in range(0,n):
            print(matriz[i][j],end="\t")
        print("")
#PRINCIPAL:
n = int(input("ingrese tamaño del vector: "))
matp = diagonalP(n)
print("matriz diagonal principal:")
imprimirm(matp,n)
mats = diagonalS(n)
print("matriz diagonal secundaria:")
imprimirm(mats,n)
matz = matrizZ(n)
print("matriz en forma Z:")
imprimirm(matz,n)
matzin = matrizZinver(n)
print("matriz Z invertida:")
imprimirm(matzin,n)