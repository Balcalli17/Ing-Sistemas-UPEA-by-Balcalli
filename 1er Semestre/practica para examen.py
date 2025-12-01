#llene la matriz diagonal principal con la serie fibonacci (posible pregunta de examen):
#FUNCIONES:
def fibonacci(n):
    fib = [0]*n
    fib[0]=1
    fib[1]=1
    for i in range (2,n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

#PRINCIPAL:
n = int(input("ingrese tamaño de la matriz:"))
vec = fibonacci(n)
print(vec)
cont = 0
matriz = [[0]*n for _ in range (n)]

for i in range (0,n):
    for j in range (0,n):
        if (i==j):
            matriz[i][j] = vec[cont]
            cont = cont + 1

for i in range (0,n):
    for j in range (0,n):
        print(matriz[i][j],end="\t")
    print("")