"""
16.Realiza una función que reciba un número n entero positivo y formar un nuevo número nn con sus dígitos primos.
(n mínimamente debe tener un dígito primo).
Ej: ENTRADA: ingrese n: 78243569 , SALIDA: nn: 7235
"""
def primo(x):
    t=0
    for i in range(1,x+1):
        d=x%i
        if(d==0):
            t=t+1
    if(t==2):
        return True

def main():
    while(True):
        x=int(input("Ingrese Número:"))
        if(x<0):
            print("Error")
        else:
            break 
    f=1 
    s=0         
    while(x>0):
        d=x%10
        p=primo(d)
        if(p):
            s=s+d*f
            f=f*10
        x=x//10    
    print("Num primo:",s)
main()