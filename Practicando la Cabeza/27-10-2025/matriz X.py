def crearm(m,n):
    for i in range(n):
        for j in range(n):
            if (i==j or i+j==n-1):
                m[i][j]=1
"""
LA FORMA DEL INGE:
def equis(m,n):
    for i in range(n):
        m[i][i]=1
        m[i][n-i-1] = 1
"""
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
    print("")
    mostrarm(m,n)
main()