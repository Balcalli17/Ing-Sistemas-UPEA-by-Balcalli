#FUNCIONES:
def moverv(vec,tam):
    aux = 1
    for i in range(tam//3):
        for j in range(i,tam,tam//3):
            vec[j] = aux
            aux += 1
    print(vec)

#PRINCIPAL:
def main():
    while(True):
        n = int(input("ingrese tamaño del vector: "))
        if (n % 3 == 0 and n > 0):
            break
        else:
            print("Error...")
    
    v = [0]*n
    moverv(v,n)
main()
