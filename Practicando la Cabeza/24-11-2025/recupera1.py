"""
Dada el vector V de tamaño N ordenar desendentemente sus elementos:
ej: N = 5
    ***Vector Creado:***
    v = [ 6  , 1  , 15 , 23 , 8 ]
    
    ***Vector Ordenado:***
    v = [ 23 , 15 , 8  , 6  , 1 ]
"""
#FUNCIONES:
def crearv(v,n):
    for i in range(n):
        v[i]=int(input(f"[{i}]="))
def mostrarv(v,n):
    for i in range(n):
        print(v[i],end="-")
    print()
def ordenarv(v,n):
    for i in range(n):
        for j in range(n-1):
            if v[j] < v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese tamaño del vector: "))
        if n > 0:
            break
        else:
            print("ingrese un valor entero positivo...")
    v=[0]*n
    crearv(v,n)
    print("***vector creado:***")
    mostrarv(v,n)
    ordenarv(v,n)
    print("***vector ordenado:***")
    mostrarv(v,n)
main()