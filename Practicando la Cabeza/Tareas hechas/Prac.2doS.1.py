#resuelve este ejercicio matematico:
#(A^B)!+(A^B)^C!
#FUNCIONES
#creamos nuestras funciones para cada operacion que se realiza en este ejercicio:
def expo(X,Y):
    exp=X**Y
    return exp

def suma(X,Y):
    sum=X+Y
    return sum

def factorial(X):
    fact=1
    for i in range (1,X+1):
        fact = fact * i
    return fact

#PRINCIPAL
#en primero, solicitamos al usuario el numero por pantalla:
A=int(input("ingrese valor de A: "))
B=int(input("ingrese valor de B: "))
C=int(input("ingrese valor de C: "))
#resolvamos la primera parte de nuestro ejercicio: (A^B)!
#para dentro del parentisis:
paso1=expo(A,B)
paso2=factorial(paso1)
#resolvamos la segunda parte de nuestro ejercicio: (A^B)^C!
paso3=expo(A,B)
pasCfact=factorial(C)
paso4=expo(paso3,pasCfact)
#como ultimo paso realizar la suma de ambos resultados: (A^B)!+(A^B)^C!
pasofinal=suma(paso2,paso4)
#por ultimos mostramos por pantalla el resultado:
print(f"el resultado es: {pasofinal}")