def fib(n):
    m = n*3
    vec = [0]*m
    vec[0]=1
    vec[1]=1
    for i in range (2,m):
        vec[i]= vec[i-1] + vec[i-2]
    return vec
#PRINCIPAL:
n = int(input("ingrese tamaño de la matriz:"))
matriz = [[0]*n for _ in range (n)]
v = fib(n)
print(v)
cont = 0
for i in range (0,n):
    for j in range (0,n):
        if (i == j) or (i >= j):
            matriz[i][j]=v[cont]
            cont = cont + 1

for i in range (0,n):
    menor = matriz[i][0]
    for j in range (0,n):
        if(matriz[i][j]<menor):
            menor=matriz[i][j]
    print(f"el menor de la fila {i} es: {menor} ")

for i in range (0,n):
    for j in range (0,n):
        print(matriz[i][j],end="\t")
    print("")
