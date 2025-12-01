#FUNCIONES:
def crear_v(dig,tam):
    for i in range(tam):
        dig[i] = 0

def mostrar_v(dig,tam):
    print(dig)
    
def fibo_vec(dig,tam):
    m = tam // 2
    a = 0
    b = 1
    for i in range(m-1,-1,-1):
        c = a+b
        dig[i] = a
        a = b
        b = c
    for i in range (m,tam,1):
        c = a + b
        dig[i] = a
        a = b
        b = c
#PRINCIPAL:
def main():
    while(True):
        tam = int(input("tamaño del vector: "))
        if tam % 2 == 0:
            break
    
    dig = [0] * tam
    crear_v(dig,tam)
#    mostrar_v(dig,tam)
    fibo_vec(dig,tam)
    mostrar_v(dig,tam)
main()