def crearm(m,n):
    mitad = (n//2) - 1
    for i in range(0,mitad+1):
        for j in range(i,n-i):
            m[i][j]=1
            m[n-i-1][j]=1
    if n % 2 == 1:
        m[mitad+1][mitad+1]=1
        
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