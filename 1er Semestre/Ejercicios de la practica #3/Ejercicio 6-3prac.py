#6. Cargar dos vectores cada uno con 5 elementos enteros y determinar si los datos almacenados en ambos vectores son exactamente los mismos tanto en contenido como en posición.
print("ingrese tamaño de los dos vectores:")
#creamos dos variables para dar el tamaño del vector.
n1 = 5
n2 = 5
#creamos el primer vector.
vector1=[0]*n1
for i in range (0,n1):
    vector1[i]=int(input(f"[{i}]="))
#imprimimos el primer vector por pantalla.
for i in range (0,n1):
    print(vector1[i],end="-")
#creamos el segundo vector.
vector2=[0]*n2
for j in range (0,n2):
    vector2[j]=int(input(f"[{j}]="))
#imprimimos el segundo vector por pantalla.
for j in range (0,n2):
    print(vector2[j],end="-")
#colocamos un "if", para comparar el primer y segundo vector si son identicos.
if vector1[i] == vector2[j]:
    print("los vectores son identicos.")
else:
    print("los vectores no son identicos.")