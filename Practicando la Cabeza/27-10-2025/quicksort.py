#FUNCIONES:
def quicksort(v,izq,der):
    i = izq
    j = der
    pivote = v[i + (j - i) // 2]
    while i <= j:
        while v[i] < pivote:
            i += 1
        while v[j] > pivote:
            j -= 1
        if (i <= j):
            v[i], v[j] = v[j], v[i]
            i += 1
            j -= 1
    if izq < j:
        quicksort(v,izq,j)
    if i < der:
        quicksort(v,i,der)

#PROGRAMA PRINCIPAL
import random
import time
n = int(input("ingrese tamaño del vector: "))
#generamos los numeros aleatorios en el vector
v = [random.randint(1,100) for i in range(n)]
print("***vector aleatorio***")
print(v)
#medir el tiempo que tarda burbuja:
inicio = time.time()
quicksort(v,0,n-1)
final = time.time()
tiempoTranscurrido = final - inicio
print("***vector ordenado***")
print(v)
print(f"el tiempo total transcurrido fue de {tiempoTranscurrido:.2f} segundos.")