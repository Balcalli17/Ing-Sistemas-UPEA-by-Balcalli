#12. Llenar un vector con números mayores a 10 y ordenar sus elementos.
#solicitamos por pantalla el tamaño del vector.
n = int(input("ingrese tamaño del vector: "))
#luego creamos el vector (y le aplicamos a condicion de solamente ingresar numeros de 2 digitos, o sea 10 en adelante).
vector=[0]*n
for i in range (0,n):
    while(True):
        vector[i]=int(input(f"[{i}]="))
        if 10 <= vector[i]:
            break
#luego con un bucle "for", aplicamos el metodo burbuja para organizar de forma ascendente.
aux = 0
for i in range (0,n):
    for j in range (0,n-1-i):
        if (vector[j] > vector[j+1]):
            aux = vector[j]
            vector[j] = vector[j+1]
            vector[j+1] = aux
#mostramos por pantalla el vector ya organizado de forma ascendente.
for i in range (0,n):
    print(vector[i],end="-")