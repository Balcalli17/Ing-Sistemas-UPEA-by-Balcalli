#FUNCIONES:
def crear_v(dig,tam):
    for i in range(tam):
        dig[i] = int(input("vec[{i}]="))

def mostrar_v(dig,tam):
    print(dig)
    
def suma_dig(dig,tam):
    for i in range(tam):
        dig[i]=sum_dig_num(dig[i])
        
def sum_dig_num(num):
    S=0
    while(num>0):
        D=num%10
        S=S+D
        num=num//10
    return S
#PRINCIPAL:
def main():
    tam = int(input("tamaño del vector: "))
    dig = [0] * tam
    crear_v(dig,tam)
    mostrar_v(dig,tam)
    suma_dig(dig,tam)
    mostrar_v(dig,tam)
main()