#FUNCIONES
def crearv(v,n):
    for i in range(n):
        v[i]=int(input(f"[{i}]="))

def mostrarv(v,n):
    for i in range(n):
        print(v[i],end="-")
    print("")
    
def ordenarv(v,ini,fin):
    for i in range(ini,fin):
        for j in range(ini,fin-(i - ini)-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] =v[j+1], v[j]
            
#PRINCIPAL
def main():
    while True:
        n = int(input("ingrese tamaño del vector: "))
        if n > 0:
            break
        else:
            print("ingrese un valor entero positivo...")
    v=[0]*n
    crearv(v,n)
    print("***vector original***")
    mostrarv(v,n)
    while True:
        a = int(input("ingrese la posicion inicial: "))
        if a >= 0:
            b = int(input("ingrese la posicion final: "))
            if b > a and b <= n:
                break
            else:
                print("ingrese el valor de ¨b¨ mayor de ¨a¨ y menor o igual al tamaño del vector ¨n¨...")
        else:
            print("el valor de a debe ser mayor o igual a 0 u/o tamaño de ¨n¨...")
    ordenarv(v,a,b+1)
    print("***vector ordenado***")
    mostrarv(v,n)
main()