# Dado un vector de números enteros desordenados, implementa un método de
# ordenación para ordenar un intervalodel vector delimitado por a y b.

# Leer los elementos de un vector
def leerVector(vector, tamaño):
    for i in range(tamaño):
        while True:
            try:
                vector[i] = int(input(f"Ingrese v[{i}]: "))
                break
            except ValueError:
                print("El valor ingresado no es válido\n")
# Ordenar los elementos de un vector de forma ascendente
def OrdenAscendente(vector, ini, fin):
    for i in range(ini, fin):
        for j in range(ini, fin -(i - ini) -1):
            if vector[j] > vector[j + 1]:
                aux = vector[j]
                vector[j] = vector[j + 1]
                vector[j + 1] = aux
# Programa Principal
def main():
    while True:
        try:
            N = int(input("Ingrese el tamaño del vector: "))
            break
        except ValueError:
            print("Ingrese solo números enteros\n")
    V = [0] * N
    leerVector(V, N)
    print(f"Vector Original: {V}\n")
    print("Ingrese a y b (el rango a ordenar del vector)")
    while True:
        try:
            a = int(input("Ingrese a: "))
            if a >= 0:
                b = int(input("Ingrese b: "))
                if b > a and b <= N:
                    break
                else:
                    print("'b' debe ser mayor a 'a' y menor al tamaño del vector\n")
            else:
                print("a debe ser mayor o igual a 0\n")
        except ValueError:
            print("Ingrese solo números enteros\n")
    OrdenAscendente(V, a, b +1)
    print(f"Vector Ordenado: {V}")
main()