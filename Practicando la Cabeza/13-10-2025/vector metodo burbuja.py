"""
Ejercicio:
Crea un vector de tamaño NxM, luego reordenar el vector de forma ascendente
(metodo burbuja).
EJ: N = 5
    V=[3,6,1,8,7]
    V=[1,3,6,7,8]                    
"""

#FUNCIONES:
# creamos una funcion para crear el vector y asignar valores
def crearv(v,n):
    for i in range(0,n,1):
        v[i] = int(input(f"[{i}]="))
#creamos una funcion para mostrar por pantalla el vector creado
def mostrarv(v,n):
    for i in range(0,n,1):
        print(v[i],end="-")
    print()
#creamos una funcion para la ordenacion del metodo burbuja
def ordenar(v,n):
    for i in range(1,n):
        for j in range(n-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
"""
#es una forma para evitar usar variables auxiliares, por el uso de consumo de memoria
para comprobarlo copia este comentario por la funcion "def ordenar" :)

def ordenar(v,n):
    for i in range(1,n):
        for j in range(n-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]

#es la forma que se enseño en el anterior semestre para realizar el metodo burbuja,
que es utilizando auxiliares. (aun que sacrificando el uso de memoria)

def ordenar(v,n):
    for i in range(0,n,1):
        for j in range(0,n-i-1,1):
            if(v[j] > v[j+1]):
                aux = v[j]
                v[j] = v[j+1]
                v[j+1] = aux
"""
#PRINCIPAL:
def main():
    while True:
        #De primero, solicitamos por pantalla el tamaño del vector
        n = int(input("ingrese tamaño del vector: "))
        #asignamos una condicion, para que solamente el usuario ingrese valores positivo
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    #creamos el vector
    v = [0]*n
    #llamamos a las funciones creadas
    print("***introduzca los valores del vector***")
    crearv(v,n)
    print("***vector original:***")
    mostrarv(v,n)
    ordenar(v,n)
    print("***vector ordenado:***")
    mostrarv(v,n)
main()