#FUNCIONES:
def crearm(m,n):
    c = 1
    arriba = 0
    abajo = n - 1
    izquier = 0
    dere = n - 1
    while izquier <= dere and arriba <= abajo:
        for i in range(arriba,abajo + 1):
            m[i][izquier]=c
            c = c + 1
        izquier = izquier + 1
        
        if izquier<=dere:
            for j in range(izquier,dere + 1):
                m[abajo][j] = c
                c = c + 1
            abajo = abajo - 1
            
def mostrarm(m,n):
    for i in range(n):
        for j in range(n):
            print(m[i][j],end="\t")
        print()
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese el tamaño de la matriz cuadrada: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
            
    m = [[0]*n for _ in range(n)]
    crearm(m,n)
    mostrarm(m,n)
main()