#leer un numero n entero positivo hallar la suma de sus digitos:
#FUNCIONES
def suma_dig(num,p):
    s = 0
    while(num > 9): 
        d = num // p
        print(d,"+",end="")
        s = s + d
        num = num % p
        p = p // 10
    s = s + num
    print(num,"=",s)
    return s

def potencia(num):
    pot = 1
    while(num > pot):
        pot = pot * 10
    pot = pot // 10
    return pot
#PRINCIPAL
while(True):
    n=int(input("ingresa el valor de n entero positivo por pantalla: "))
    if n > 0:
        break
    
poten = potencia(n)

sum = suma_dig(n,poten)
