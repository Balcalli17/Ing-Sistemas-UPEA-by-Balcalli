"""
1.generar la matriz M de tamaño NxM (llenar solamente la diagonal principal):
ej: N = 4
        [ 2 , 0 , 0 , 0 ]
        [ 0 , 4 , 0 , 0 ]
        [ 0 , 0 , 6 , 0 ]
        [ 0 , 0 , 0 , 8 ]
"""
#FUNCIONES:
#creacion de una matriz:
def crearm(m,n):
    x = 2
    for i in range(n):
        for j in range(n):
            if (m[i] == m[j]):
                m[i][j] = x
                x = x + 2
"""
°este metodo es para realizar el llenado en el diagonal principal de la forma del ingeniero
(se puede reducir el llenado de la matriz de 0 con el "for") de una manera para reducir el
consumo de memoria:

def crearm(m,n):
    for i in range(n):
        for j in range(n):
            m[i][j] = 0
    
    for i in range(n):
        m[i][i] = 2 * i + 2
"""
#mostrar la matriz:
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
    print("***matriz creada llenado diagonal principal***")
    mostrarm(m,n)
main()