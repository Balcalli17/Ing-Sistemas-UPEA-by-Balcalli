#Realice una función que reciba como parámetro un número x mayor a cero y a partir del mismo muestre la cuenta regresiva hasta llegar a 0, este resultado se mostrará separado por comas.
#X = 9    Salida: 9,8,7,6,5,4,3,2,1,0
#FUNCIONES:
def serie(n):
    cont=n
    aux = 0
    while(aux<=cont):
        print(cont,end=",")
        cont = cont - 1

#PRINCIPAL:
def main():
    while(True):
        X = int(input("ingrese valor de X entero positivo:"))
        if (X>=0):
            break
    print("la serie es: ",end="")
    serie(X)

main()

