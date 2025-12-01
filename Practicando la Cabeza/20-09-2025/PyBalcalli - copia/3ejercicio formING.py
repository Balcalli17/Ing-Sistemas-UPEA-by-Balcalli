def moverv(vec,tam):
    p1 = tam // 3
    p2 = tam - p1
    cont = 1
    for i in range(0,p1,1):
        vec[i] = cont
        cont = cont + 1
        vec[p1] = cont
        cont = cont + 1
        vec[p2] = cont
        cont = cont + 1
        p1 = p1 + 1
        p2 = p2 + 1
    return vec

def mostrarv(vec,tam):
    print(vec)

def main():
    while(True):
        n = int(input("ingrese tamaño del vector (multiplo de 3): "))
        if (n % 3 == 0 and n > 0):
            break
        else:
            print("Error...")
    
    v = [0]*n
    a = moverv(v,n)
    mostrarv(a,n)
main()