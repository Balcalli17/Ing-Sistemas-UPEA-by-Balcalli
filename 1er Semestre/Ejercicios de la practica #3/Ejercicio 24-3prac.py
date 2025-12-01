#24. Introducir a un vector n notas de los estudiantes de la materia Programación, hallar el mayor, menor de las notas ingresadas.
#solicitamos por pantalla el tamaño del vector.
n = int(input("ingrese tamaño del vector: "))
#creamos el vector con las notas de los estudiantes.
vector=[0]*n
print("ingrese notas de los estudiantes:")
for i in range (0,n):
    vector[i]=int(input(f"[{i}]="))
#mostramos por pantalla la notas de los estudiantes.
print("notas de los estudiantes:")
for i in range (0,n):
    print(vector[i],end=" - ")
print("")
#usamos un bucle "for" para realizar la condicion.
mayor=vector[0] #creamos 2 variables y le asignamos el valor del 1er vector a ambas.
menor=vector[0]
for i in range (0,n):
    if vector[i] > mayor: #condicion: si todo el vector[i] es "mayor" a mayor se actualiza la variable "mayor".
        mayor = vector[i]
    elif vector[i] < menor: #sino, si vector[i] es menor a "menor" se actualiza la variable "menor".
        menor = vector[i]
        #ademas, como se encuentra en el bucle "for", va a recorrer el vector hasta que "i" sea mayor a "n".
#por ultimo se muestra por pantalla, los resultados de este ejercicio.
print(f"el mayor es: {mayor}")
print(f"el menor es: {menor}")
