#leer n entero positivo y hallar la suma de los factoriales de cada digito
#FUNCIONES
def suma_fac(num):
    fact = 1
    s = 0 
    while(num > 0):
        d = num % 10
        print(d,end="!+")
        for i in range (1,d+1):
            fact = fact * i
        s = s + fact
        fact = 1
        num = num // 10
    return s
#PRINCIPAL
while(True):
    n=int(input("ingresa el valor de n entero positivo por pantalla: "))
    if n > 0:
        break
    
sum = suma_fac(n)
    
print("=",sum)