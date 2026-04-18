class Numeros_Naturales():
    def __init__(self, numero):
        self.numero=numero
    def es_primo(self, x):
        d=0
        for i in range(1,x+1,1):
            if x%i==0:
                d=d+1
        if d==2:
            return True
        else:
            return False
    def Es_Capicua(self,x):
        y=x
        nn=0
        while y>0:
            dig=y%10
            nn=nn*10+dig
            y=y//10
        if nn==x:
            return True
        else:
            return False
    def Numero_Par(self,n):
        if n%2==0:
            return True
        else:
            return False
    def Numero_impar(self,x):
        if x%2==1:
            return True
        else:
            return False
    def Es_Multiplo_n(self,x,num):
        if x%num==0:
            return True
        else:
            return False

n=int(input("Ingrese un numero: "))
objeto1=Numeros_Naturales(n)
if objeto1.es_primo(n):
    print("Es primo")
else:
    print("No es primo")
if objeto1.Es_Capicua(n):
    print("Es capicua")
else:
    print("No es capicua")
if objeto1.Numero_Par(n):
    print("Es par")
else:
    print("No es par")
if objeto1.Numero_impar(n):
    print("Es impar")
else:
    print("No es impar")
sum=int(input(f"Ingrese un numero para verificar si {n} es multiplo de este numero: "))
if objeto1.Es_Multiplo_n(n,sum):
    print("Es multiplo")
else:
    print("No es multiplo")