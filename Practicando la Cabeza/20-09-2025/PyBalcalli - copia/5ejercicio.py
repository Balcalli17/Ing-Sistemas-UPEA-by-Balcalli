"""
Dado el vector V de tamaño n, mostrar los elementos que son numeros capicua
ENTRADA: n = 5  ,SALIDA: v=15,202,73,8,667    mostrar: 202,8
"""
#FUNCIONES:
def crearv(vec,tam):
    for i in range(tam):
        vec[i] = int(input(f"[{i}]="))

def mostrarv(vec,tam):
    print(vec)

def capicua(num):
    aux = num
    r = 0
    while(num > 0):
        d = num % 10
        r = r*10+d
        num = num // 10
    if aux == r:
        return 1
    else:
        return 0
        
def muestra_cap(vec,tam):
    for i in range(0,tam,1):
        if capicua(vec[i]) == 1:
            print(vec[i],end=",")
#PRINCIPAL:
def main():
    while(True):
        n = int(input("ingrese el tamaño del vector: "))
        if n > 0:
            break
        else:
            print("Error...")
    
    v = [0]*n
    crearv(v,n)
    print("vector creado:")
    mostrarv(v,n)
    print("numeros capicuas: ")
    muestra_cap(v,n)
main()
