def crearm(m, n):
    c = 1
    for j in range(n):  # recorrer columnas
        if j % 2 == 0:
            # columnas pares: de abajo hacia arriba
            for i in range(n-1, -1, -1):
                m[i][j] = c
                c += 1
        else:
            # columnas impares: de arriba hacia abajo
            for i in range(n):
                m[i][j] = c
                c += 1


def mostrarm(m, n):
    for i in range(n):
        for j in range(n):
            print("%5d" % m[i][j], end="")
        print()
def main():
    while True:
        n = int(input("Ingrese tamaño de la matriz cuadrática: "))
        if n > 0:
            break
        else:
            print("Ingrese un valor positivo...")

    m = [[0] * n for _ in range(n)]
    crearm(m, n)
    mostrarm(m, n)
main()
