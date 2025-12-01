"""
1.Dado un vector con n elementos, reemplaza sus elementos por el PRIMER DÍGITO de cada elemento.
ej:ENTRADA: vector creado: [12,11,1,10,21] ,SALIDA: [1,1,1,1,2]
"""
def crear_v(dig,tam):
    for i in range(tam):
        dig[i] = int(input("vec[{i}]="))

def mostrar_v(dig,tam):
    print(dig)
    
def pd_vec(dig,tam):
    for i in range(tam):
        while(dig[i]>9):
            dig[i]=dig[i] // 10
    return dig
#PRINCIPAL:
def main():
    tam = int(input("tamaño del vector: "))
    dig = [0] * tam
    crear_v(dig,tam)
    mostrar_v(dig,tam)
    pd_vec(dig,tam)
    mostrar_v(dig,tam)
main()