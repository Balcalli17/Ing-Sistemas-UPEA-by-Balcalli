"""
llenar las edades de n estudiante en el vector EDAD:
n = 6  ,  vec = 15,10,20,8,14,7  ,SALIDA: 15,7,10,20,8,14
"""
#FUNCIONES:
def crearv(vec,tam):
    for i in range(tam):
        vec[i] = int(input(f"[{i}]="))

def mostrarv(vec,tam):
    print(vec)

def imparv(vec,tam):
    aux = 0
    for i in range(tam):
        if (vec[i] % 2 == 0):
            aux = vec[i]
            vec[0] = aux
            aux = 0

#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese el tamaño de n estudiante: "))
        if n > 0:
            break
    v = [0]*n
    crearv(v,n)
    print("vector creado: ")
    mostrarv(v,n)
    imparv(v,n)
    print("nuevo vector: ")
    mostrarv(v,n)
main()

#ANALIZAR...