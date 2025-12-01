"""
Tarea para la casa:
1. Llenar las edades de N estudiantes en un vector EDAD:
ej: N = 6 , EDAD: [15,10,20,8,14,7]
llenar las edades impares a la izquierda, y las edades pares a la derecha.
EDAD: [15,7,10,20,8,14]
"""
# FUNCIONES:
def crearv(vec, tam): #Creamos una funcion para crear un vector
    for i in range(tam):
        vec[i] = int(input(f"[{i}] = "))

def mostrarv(vec, tam): #esta funcion es solo para mostrar el vector en la pantalla
    print(vec)

def reordenar(vec, tam): # creamos una funcion con la condicion para reordenar
    i = 0
    j = tam - 1
    while i < j:
        # avanzar si ya hay impar a la izquierda
        while i < tam and vec[i] % 2 != 0:
            i += 1
        # retroceder si ya hay par a la derecha
        while j >= 0 and vec[j] % 2 == 0:
            j -= 1
        # si aún no se cruzan, intercambiar
        if i < j:
            aux = vec[i]
            vec[i] = vec[j]
            vec[j] = aux
# PRINCIPAL:
def main():
    while True:
        n = int(input("Ingrese la cantidad de estudiantes para registrar: "))
        if n > 0:
            break
        else:
            print("Ingrese un número positivo...")
    v = [0] * n
    crearv(v, n)
    print("Vector ingresado:")
    mostrarv(v, n)
    reordenar(v, n)
    print("Vector reordenado (impares izquierda, pares derecha):")
    mostrarv(v, n)
main()