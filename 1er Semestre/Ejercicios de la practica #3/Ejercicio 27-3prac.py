#27. Capturar el tamaño de un vector por pantalla y calcular la suma de los cuadrados usando for y funciones.
#FUNCIONES:
#creamos una funcion para crear un vector.
def crearv(n):
    vector=[0]*n
    for i in range (0,n):
        vector[i]=int(input(f"[{i}]="))
    return vector
#creamos una funcion para imprimir el vector creado y mostrar por pantalla.
def imprimirv(vector,n):
    for i in range(0,n):
        print(vector[i],end=" - ")
    print("")
#PRINCIPAL:
#solicitamos por pantalla el tamaño del vector.
n = int(input("ingrese tamaño del vector: "))
#asignamos a una variable la funcion(crearv), y a la funcion le damos "n".
vec = crearv(n)
#llamamos directamente la funcion (imprimirv) y le asignamos variables "vec" y "n".
print("vector generado:")
imprimirv(vec,n)
#creamos la condicion en un bucle "for", y una variable "suma" para este procedimiento.
suma = 0
for i in range (0,n):
    suma = suma + vec[i]
#mostramos por pantalla la suma de los vectores.
print(f"la suma de los valores del vector creado es: {suma}")