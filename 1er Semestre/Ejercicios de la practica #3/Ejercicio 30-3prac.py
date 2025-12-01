#30. Capturar el tamaño de un vector por pantalla y generar un vector aleatorio y encontrar el primer número divisible por 7 usando while y funciones.
#FUNCIONES:
def crearv(n):
    vector=[0]*n
    for i in range (0,n):
        vector[i]=int(input(f"[{i}]="))
    return vector

def mostrarv(vector,n):
    for i in range (0,n):
        print(vector[i],end=" - ")
    print("")

def div_7(vector,n):
    aux = 0
    for i in range (0,n):
        while aux < len(vector[i]):
            if vector[i] % 7 == 0:
                return vector[i]
        aux = aux + 1
    return None

#PRINCIPAL:
n = int(input("ingrese tamaño del vector: "))
vec = crearv(n)
print("vector generado.")
mostrarv(vec,n)

divisible = div_7(vec,n)
if divisible is not None:
    print("el primer numero divisible de 7 es:",divisible)
else:
    print("no se encontro numeros divisibles de 7.")