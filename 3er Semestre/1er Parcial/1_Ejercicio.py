"""
1 Defina la clase Dígitos, cuyo atributo sea un número entero y defina los siguientes métodos:
a) Invertir un número
b) Encontrar el dígito mayor
c) Encontrar el dígito menor
d) Encontrar la cantidad de dígitos de un número.
e) Contar la cantidad de dígitos primos
f) Conformar un nuevo número con los dígitos primos del número.
g) Eliminar el i-ésimo dígito.
"""
class Digito: 
    def __init__(self, numero):
        self.numero=numero 
    def Invertir_Numero(self):
        nn=0
        aux=abs(self.numero)
        while aux >0:
            dig=aux%10
            nn=nn*10+dig
            aux=aux//10
        return nn if self.numero>=0 else -nn
    def Digito_Mayor(self):
        may=0
        nn=0
        aux=abs(self.numero)
        while aux>0:
            dig=aux%10
            if dig>may:
                may=dig
            aux=aux//10
        return may
    def Digito_Menor(self):
        me=9
        aux=abs(self.numero)
        while aux>0:
            dig=aux%10
            if dig<me:
                me=dig
            aux=aux//10
        return me
    def Cantidad_Digitos(self):
        cd=0
        aux=abs(self.numero)
        while aux>0:
            aux=aux//10
            cd=cd+1
        return cd
    def Cantidad_digitosprimos(self):
        cp=0
        aux=abs(self.numero)
        while aux>0:
            dig=aux%10
            d=0
            for i in range(1,dig+1,1):
                if dig%i==0:
                    d=d+1
            aux=aux//10
            if d==2:
                cp=cp+1
        return cp
    def nn_primos(self):
        nn=0
        p=1
        aux=abs(self.numero)
        while aux>0:
            dig=aux%10
            d=0
            for i in range(1,dig+1,1):
                if dig%i==0:
                    d=d+1
            aux=aux//10
            if d==2:
               nn=(dig*p)+nn
               p=p*10
        return nn
    def eliminar_numero(self,x):
        cant=self.Cantidad_Digitos()
        if x>cant or x<=0: return self.numero
        nuevo=0
        posicion=1
        aux=abs(self.numero)
        contador_pos=1
        while aux>0:
            d=aux%10
            if contador_pos!=x:
                nuevo=(d*posicion)+nuevo
                posicion=posicion*10
            aux=aux//10
            contador_pos=contador_pos+1
        return nuevo if self.numero>=0 else -nuevo
def main():
    n=int(input("Ingrese un numero: "))
    objeto=Digito(n)
    print(f"El numero invertido es: {objeto.Invertir_Numero()}")
    print(f"El digito mayor del numero es: {objeto.Digito_Mayor()}")
    print(f"El digito menor del numero es: {objeto.Digito_Menor()}")
    print(f"La cantidad de digitos es: {objeto.Cantidad_Digitos()}")
    print(f"La cantidad de numeros primos es: {objeto.Cantidad_digitosprimos()}")
    print(f"El nuevo numero de primos es: {objeto.nn_primos()}")
    x=int(input("Eliminar el x digito: "))
    print(f"El numero eliminado es {x}, nuevo numero es {objeto.eliminar_numero(x)}")
main()