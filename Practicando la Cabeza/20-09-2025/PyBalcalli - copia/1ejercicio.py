#FUNCIONES:
def crearv(tam,vec): #Una funcion para crear el vector
    for i in range(tam): 
        vec[i]=int(input(f"[{i}]="))

def mostrarv(tam,vec): #una funcion para mostrar el vector
    print(vec)

def moverv(tam,vec): # creamos una funcion para colocar la condicion
    m = tam // 2 - 1
    cont = 1
    for i in range(0,m+1,1):
        vec[i] = cont
        cont = cont + 1
        vec[tam-i-1] = cont
        cont = cont + 1
    if tam % 2 == 1:
        vec[m+1] = cont
    return vec
#PRINCIPAL:
def main():
    while(True):
        n = int(input("ingrese el tamaño del vector: "))
        if n > 0:
            break
        else:
            print("Error...")
    
    vec = [0]*n
#    crearv(n,vec)
    moverv(n,vec)
    mostrarv(n,vec)
main()
