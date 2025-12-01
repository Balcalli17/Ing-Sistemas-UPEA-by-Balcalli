#Funciones:
def crear_par_v(n):
    vc = [0] * n
    for i in range(0,n):
        vc[i] = 2 * i + 2
    return vc

def mostrar_v(n,vc):
    for i in range (0,n):
        print(vc[i],end="-")
#Principal:
def main():
    while(True):
        try:
            n = int(input("ingrese tamaño del vector n entero positivo:"))
            if n > 0:
                break
            else:
                print("no es un numero positivo.")
        except ValueError:
            print("error: ingrese solamente numeros.")
            
    a = crear_par_v(n)
    mostrar_v(n,a)

main()
    