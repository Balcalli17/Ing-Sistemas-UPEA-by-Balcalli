#FUNCIONES:
def burbuja(v,n):
    for i in range(1,n):
        for j in range(0,n-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]

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
burbuja(v,n)
final = time.time()
tiempoTranscurrido = final - inicio
print("***vector ordenado***")
print(v)
print(f"el tiempo total transcurrido fue de {tiempoTranscurrido:.2f} segundos.")