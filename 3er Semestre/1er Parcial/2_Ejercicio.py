class Calculadora: 
    def __init__(self, numero1, numero2):
        self.numero1=numero1
        self.numero2=numero2
    def suma(self):
        return (f"La suma es: {self.numero1+self.numero2}")
    def resta(self):
        return (self.numero1-self.numero2)
    def multiplicacion(self):
        return (self.numero1*self.numero2)
    def division(self):
        if self.numero2!=0:
             return (self.numero1/self.numero2)
        else: 
            print("No se puede dividir entre 0")
def menu():
    print("\n   MENU CALCULADORA ")
    print("1. SUMA ")
    print("2. RESTA ")
    print("3. MULTIPLICACION ")
    print("4. DIVISION ")
    print("5. SALIR ")
    return int(input("Ingrese un valor: "))
opcion=0
while opcion !=5:
    opcion=menu()
    if opcion>=1 and opcion <=4:
        valor1=float(input("Ingrese el primer dato: "))
        valor2=float(input("Ingrese el segundo dato: "))
        mi_calculadora=Calculadora(valor1, valor2)  
        if opcion==1:
            print(mi_calculadora.suma())  
        if opcion==2:
            print(mi_calculadora.resta()) 
        if opcion==3:
            print(mi_calculadora.multiplicaion())
        if opcion==4:
            print(mi_calculadora.division())  
print("Programa terminado")