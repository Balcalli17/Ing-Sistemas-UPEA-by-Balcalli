"""
3.Cargue un vector con N elementos introducidos por teclado y genere otro vector con los cuadrados de
cada elemento contenidos en el primer vector.Muestre el vector origen y el vector resultado generado.
ej: ENTRADA: numeros ingresados:[4,10,3,6,5] ,SALIDA: [16,100,9,36,25]
"""
#FUNCIONES:
def crearv(dig,tam):
    for i in range(tam):
        dig[i]=int(input(f"[{i}]="))

def imprimirv(dig,tam):
        print(dig)

def mult_vec(dig,tam):
    for i in range(tam):
        dig[i]=dig[i]*dig[i]
    return dig
#PRINCIPAL:
def main():
    tam=int(input("ingrese tamaño del vector: "))
    dig=[0]*tam
    crearv(dig,tam)
    imprimirv(dig,tam)
    mult_vec(dig,tam)
    imprimirv(dig,tam)
main()

