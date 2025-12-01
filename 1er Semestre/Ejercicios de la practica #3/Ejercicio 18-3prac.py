#18. Dado el vector V de tamaño N con elementos enteros positivos, buscar el primer número primo y a partir de ese número rotar los elementos restantes hacia la izquierda. De no existir ningún número primo en el vector hallar el promedio.
#FUNCIONES:
def crearvector(n): #creamos una funcion para crear un vector
    vector=[0]*n
    for i in range (0,n):
        vector[i]=int(input(f"[{i}]="))
    return vector

def imprimirvector(vector,n): #creamos una funcion para imprimir el vector por pantalla (llamamos a vector y el tamaño del vector "n")
    for i in range(0,n):
        print(vector[i],end=" - ")
    print("")

def primo(num): #creamos una funcion para hallar numeros primos.
    if (num<2):
        return False
    else:
        cont = 0
        for i in range(1,num+1):
            if (num % i == 0):
                cont = cont + 1
        if (cont==2):
            return True
        else:
            return False

#PRINCIPAL:
n = int(input("ingrese tamaño del vector: ")) #ingresamos el tamaño del vector por pantalla.
vec = crearvector(n) #llamamos la funcion (crearvector) y le asignamos la variable "n",para colocar en una variable.
imprimirvector(vec,n) #mostramos por pantalla la funcion (imprimirvector) y le asignamos "vec" y "n".
pos = -1
for i in range (0,n):
    if (primo(vec[i])):
        pos = i
        break

if (pos != -1):
    aux = vec[pos]
    for i in range (pos,n-1):
        vec[i]=vec[i+1]
    vec[n-1] = aux
    print("vector modificado:")
    imprimirvector(vec,n)
else:
    suma = 0
    for i in range (0,n):
        suma = suma + vec[i]
    promedio = suma // n
    imprimirvector(vec,n)
    print(f"el promedio es: {promedio}")