#Leer dos numeros enteros positivos y hallar la suma de sus digitos mayores:
#FUNCIONES:
def dig_izq(X):
    while(True):
        num = X / 10
        if num <= 1 and num <= 9:
            break
#solicitamos dos numeros por pantalla:
while(True):
    n=int(input("ingrese el valor de n: "))
    m=int(input("ingrese el valor de m: "))
    if n>0 and m>0:
        break

num1=dig_izq(n)
num2=dig_izq(m)

print(f"el mayor es 1: ¨{num1}")
print(f"el mayor es 2: ¨{num2}")