#9. Leer n números enteros, almacenarlos en un vector y determinar si el promedio entero de dichos números es un número primo.
#solicitamos por pantalla el tamaño del vector a crear.
n = int(input("ingrese tamaño del vector: "))
#creamos un vector.
vector=[0]*n
for i in range (0,n):
    vector[i]=int(input(f"[{i}]="))
#realizamos un bucle "for", para realizar la suma de los vectores a una variable "suma".
suma = 0
for i in range (0,n):
    if i < n:
        suma = suma + vector[i]
#realizamos la division de "suma" por el tamaño del vector, o sea "n".
promedio = suma // n
print("el promedio es: ",promedio)
#ahora verificamos si en la variable promedio es un numero primo.
cont = 0 #creamos un auxiliar para guardar el mod.
for i in range(1,promedio+1):
    if promedio%i==0:
        cont=cont+1
if cont == 2:
    print("es un numero primo")
else:
    print("no es un numero primo")

