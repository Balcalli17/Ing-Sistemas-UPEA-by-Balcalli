"""
15.Utilizando programación modular, determinar si un número es capicúa 
(se lee igual de izquierda a derecha que de derecha a izquierda).
ej : ENTRADA: 12321 - 12546 , SALIDA: es capicua - no es capicua
"""
#FUNCIONES:
def inversor(x):
    y=x
    t=0
    s=0
    while(x>0):
        t=t+1
        x=x//10
    while(y>0):
        f=1
        d=y%10
        for i in range (1,t):
            f=f*10
        s=s+d*f
        t=t-1
        y=y//10    
    return s
#PRINCIPAL:
def main():
     while(True):
         x=int(input("Ingrese Número:"))
         if(x<0):
             print("Error")
         else:
             break  
     y=inversor(x)
     if(x==y):
         print("Es capicua")
     else:
         print("No es capicua")
main()