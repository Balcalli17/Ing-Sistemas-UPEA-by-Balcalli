#15. Dado un vector de n obtener tres vectores, el primero con múltiplos de 3 el segundo con múltiplos de 5 y el ultimo con elementos que no sean múltiplos de 3 ni de 5.
#solicitamos por pantalla el tamaño del vector.
n = int(input("ingrese tamaño del vector: "))
#creamos el vector "n":
vector=[0]*n
for i in range (0,n):
    vector[i]=int(input(f"[{i}]="))
#mostramos el vector por pantalla.
print("vector creado:")
for i in range (0,n):
    print(vector[i],end="-")
print("")
#ahora con un bucle "for", creamos la condicion del ejercicio.
for i in range (0,n):
    if vector[i] % 3 == 0:
        print("los multiplos de 3 son:",vector[i])
    elif vector[i] % 5 == 0:
        print("los multiplos de 5 son:",vector[i])
    else:
        print("residuos de la operacion:",vector[i])
