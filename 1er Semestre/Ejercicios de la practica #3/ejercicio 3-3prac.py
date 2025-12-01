#3. Dado un vector N, mueve el primer elemento al final y los demás elementos a una posición anterior (rotar vector)
#pedimos por pantalla el tamaño del vector.
n = int(input("ingrese tamaño del vector: "))
#creamos el vector.
vector = [0]*n
for i in range (0,n):
    vector[i]= int(input(f"[{i}]="))
#sacamos el primer vector en una variable.
primero = vector[0]
#movemos los demas elementos una posicion a la izquierda.
for i in range (0,n-1):
    vector[i]=vector[i+1]
#colocamos el primer vector (antes guardada en una variable) al final del vector.
vector[n-1]=primero
#imprimimos el vector ya con la condicion aplicada.
for i in range (0,n):
    print(vector[i],end="-")


