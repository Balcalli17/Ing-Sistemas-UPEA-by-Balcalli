def rotardesdeprimo(v,n):
    i = 0
    while i<=n-1 and primo(v[i]) == False:
        i += 1
    if i<= n-1:
        aux = v[i]
        for j in range(i, n-1):
            v[j] = v[j+1]
        v[n-1] = aux
    else:
        print("en el vector no hay numeros primos...")

def primo(num):
    c = 0
    for i in range(1,num+1):
        if num % i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

def leervector(v,n):
    for i in range(n):
        v[i] = int(input(f"v[{i}]="))

def mostrarv(v,n):
    for i in range(n):
        print(v[i],end="-")
        
def main():
    while True:
        n = int(input("ingrese tamaño del vector: "))
        if n > 0:
            break
        else:
            print("ingrese un numero positivo...")
    v = [0]*n         
    leervector(v,n)
    rotardesdeprimo(v,n)
    mostrarv(v,n)
main()