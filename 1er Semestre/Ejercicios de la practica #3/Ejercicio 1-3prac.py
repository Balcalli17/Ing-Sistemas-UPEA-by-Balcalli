#1.Dado un Vector N, crea la función para llenar y mostrar el 2do elemento mayor del vector, llamar en la función principal.
def crearvect(n): #creamos una funcion para crear un vector
    vector=[0]*n
    for i in range (0,n):
        vector[i]=int(input(f"[{i}]="))
    return vector

def seg_mayor(vector):#creamos una funcion para hallar el segundo mayor numero.
    #creamos dos variables para realizar la condicion.
    mayor = 0
    segundo = 0
    #usamos un bucle "for", y revisamos cada numero en el vector creado.
    for num in vector:
        if num > mayor: #si "num" es mayor a "mayor",reemplazamos.
            segundo = mayor
            mayor = num
        elif num > segundo and num != mayor: #si no es el mayor, pero es mayor que el segundo y distinto al mayor,reemplazamos.
            segundo = num
    return segundo
#-----------------------------------------------------------------------------------------------------------------------------------------
#PRINCIPAL:
#solicitamos tamaño del vector
n = int(input("ingrese tamaño del vector: "))
vec=crearvect(n) #reemplazamos una funcion en una variable.
print("vector ingresado:",vec)#imprimimos por pantalla el vector creado.
seg = seg_mayor(vec) #reemplazamos la funcion de hallar el segundo mayor en una variable.
print("el segundo numero mayor es:",seg) #imprimimos por pantalla nuestro resultado.
