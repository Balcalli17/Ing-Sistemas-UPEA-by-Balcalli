"""
ejercicio:
Crea un vector de tamaño N (solamente de numeros pares), y reordenar de forma ascendente
de la siguinte manera:
ej: N = 6
    v=[ 1 , 3 , 6 , 10 , 8 , 7 ]
      |se conserva| se ordena  |
      
SALIDA: v=[ 1 , 3 , 6 , 7 , 8 , 10 ]
"""
#FUNCIONES:
def crearv(v,n):
    for i in range(0,n,1):
        v[i] = int(input(f"[{i}]="))

def mostrarv(v,n):
    for i in range(n):
        print(v[i],end="-")
    print()
"""
·en esta ocasion, se utiliza una variable para dividir un vector a la mitad
pero analizando se puede utilizar en si para dividir en varias partes de un vector
utilizando "m = n // 2" al cual el "2" podemos dividir en varias partes, por decir
partir el vector en 3, o partir en cuatro, etc... pero considerando el tamaño del
vector.
"""
def ordenar(v,n):
    m = n // 2
    for i in range(1,n):
        for j in range(m,n-1,1):
            if (v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese el tamaño del vector (numeros pares): "))
        if n % 2 == 0:
            break
        else:
            print("ingrese un numero par...")
    v = [0]*n
    crearv(v,n)
    mostrarv(v,n)
    ordenar(v,n)
    mostrarv(v,n)
main()