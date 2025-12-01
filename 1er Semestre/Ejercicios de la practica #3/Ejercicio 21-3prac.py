#21. Se desea almacenar en un vector V[ ], las notas de n estudiantes.
#FUNCIONES:
def crearv(n): #creamos una funcion para crear un vector
    v=[0]*n
    print("ingrese la nota:")
    for i in range (0,n):
        v[i]=int(input(f"[{i}]="))
    return v

def imprimirv(v,n): #creamos una funcion para mostrar por pantalla el vector.
    for i in range (0,n):
        print(v[i],end=" - ")
    print("")
#PRINCIPAL:
#solicitamos por pantalla el tamaño del vector:
n = int(input("ingrese el tamaño del vector: "))
#a una variable le asignamos la funcion "creav".
vec = crearv(n)
#mostrarmos por pantalla el resultado de este ejercicio y llamamos la funcion "imprimirv" para mostrar el vector.
print("notas del estudiante:")
imprimirv(vec,n)