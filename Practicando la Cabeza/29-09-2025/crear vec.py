
def crear_v(x):
    vec = [0] * x
    for i in range(0,x):
        vec[i] = int(input("vec[{i}]="))
    return vec
    
def mostrar_v(x,vec):
    for i in range(0,x):
        print(vec[i],end="-")
        
        
def main():
    n = int(input("ingrese el tamaño del vector"))
    a = crear_v(n)
    mostrar_v(n,a) 
main()