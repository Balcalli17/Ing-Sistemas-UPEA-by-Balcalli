"""
Ejercicio para Casa:
Crea un vector de tamaño N (multiplo de 3), luego reordenar el vector de forma ascendente
y desendente utilizando metodo burbuja:
EJ = N 12
        v=[7,12,3,5,9,8,5,7,11,20,9,5]
          |  desen | ascen |  desen  |

SALIDA: v=[12,7,5,3,5,7,8,9,20,11,9,5]
"""
#FUNCIONES:
def crearv(v,n):
    for i in range(0,n,1):
        v[i] = int(input(f"[{i}]="))

def mostrarv(v,n):
    for i in range(n):
        print(v[i],end="-")
    print()

def ordenar(v,n):
    t = n // 3
    t2 = t * 2
    for i in range(0,t-1,1):
        for j in range(0,t-1,1):
            if v[j] < v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                
    for i in range(t,t2-1,1):
        for j in range(t,t2-1,1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                
    for i in range(t2,n-1,1):
        for j in range(t2,n-1,1):
            if v[j] < v[j+1]:
                v[j], v[j+1]= v[j+1], v[j]
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese el tamaño del vector (numeros multiplos de 3): "))
        if n % 3 == 0:
            break
        else:
            print("ingrese un numero par...")
    v = [0]*n
    print("***ingrese los valores del vector:***")
    crearv(v,n)
    print("***vector original:***")
    mostrarv(v,n)
    ordenar(v,n)
    print("***vector ordenado:***")
    mostrarv(v,n)
main()