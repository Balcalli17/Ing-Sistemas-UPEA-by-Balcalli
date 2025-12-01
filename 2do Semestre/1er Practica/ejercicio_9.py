#Realiza las funciones necesarias para calcular la suma de N términos de la serie armónica:
#ejemplo: 1,1/2,1/3,...,1/n...
#n = 4    resultado de la suma: 2.08333
#FUNCIONES:
def sum_fracciones(x):
    suma = 0
    aux = 0
    for i in range (1,x+1):
        aux = 1 / i
        print(aux,end="")
        print("")
        suma = suma + aux

    return suma
#PRINCIPAL:
def main():
    while(True):
        n = int(input("ingrese el valor de n entero positivo: "))
        if (n>0):
            break
    
    result = sum_fracciones(n)
    
    print(f"el resultado de la suma de fracciones es: {result}")

main()