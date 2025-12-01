def mostrarv(tam,vec): 
    print(vec)

def moverv(tam,vec):
    m = tam // 2 - 1
    a = 0
    b = 1
    for i in range(0,m+1,1):
        c = a + b
        vec[i] = a
        a = b
        b = c
        c = a + b
        vec[tam-i-1] = a
        a = b
        b = c
    if tam % 2 == 1:
        vec[m+1] = a
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
    moverv(n,vec)
    mostrarv(n,vec)
main()
