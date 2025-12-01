#POR CORREGIR (HAY RESPUESTA CORRECTA EN FOTO...)
#FUNCIONES:
def crearv(v,n):
    for i in range(n):
        v[i] = int(input(f"[{i}]="))
        
def mostrarv(v,n):
    for i in range(n):
        print(v[i],end="-")
    print("")
        
def rotarizq(v,n):
    i = 0
    while i <= n-1 and primo(v[i]) == False:
        i += 1
    if i <= n-1:
        aux = v[i]
        for i in range(0,n-1,1):
            v[i] = v[i+1]
        v[n-1] = aux
    else:
        print("no hay numeros primos")

def primo(num):
    cont = 0
    for i in range(1,num+1):
        if num % i == 0:
            cont += 1
    if cont == 2:
        return True
    else:
        return False
            
#PRINCIPAL:
def main():
    while True:
        n = int(input("ingrese tamaño del vector: "))
        if n > 0:
            break
        else:
            print("ingrese un valor positivo...")
    v = [0] * n
    crearv(v,n)
    print("***vector creado***")
    mostrarv(v,n)
    rotarizq(v,n)
    print("***vector ordenado***")
    mostrarv(v,n)
main()