def crearm(m, n):
    c = 1
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while left <= right and top <= bottom:
        # bajar por la columna 'left'
        for i in range(top, bottom + 1):
            m[i][left] = c
            c += 1
        left += 1

        # avanzar por la fila 'bottom'
        if left <= right:
            for j in range(left, right + 1):
                m[bottom][j] = c
                c += 1
            bottom -= 1


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
