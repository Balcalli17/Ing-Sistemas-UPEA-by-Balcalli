#FUNCIONES Y POO:
class Circulo:
    def __init__(self):
        self.posx = 0
        self.posy = 0
        self.radio = 0
        
    def leer(self):
        self.posx = int(input("ingrese la posicion de x: "))
        self.posy = int(input("ingrese la posicion de y: "))
        self.radio = int(input("ingrese el tamaño de la radio: "))
    
    def mostrar(self):
        print("===== MOSTRANDO LOS DATOS: =====")
        print(f"Posicion X: {self.posx}")
        print(f"Posicion Y: {self.posy}")
        print(f"Radio: {self.radio}")

    def area(self):
        area = 3.1416 * (self.radio ** 2)
        print(f"El area del circulo es: {area}")

    def circunferencia(self):
        cir = 2 * 3.1416 * self.radio
        print(f"La circunferencia del circulo es: {cir}")

    def diametro(self):
        diam = 2 * self.radio
        print(f"El diametro del circulo es: {diam}")
#PRINCIPAL:
def main():
    print("=== CIRCULO 1 ===")
    circulo1 = Circulo()
    circulo1.leer()
    circulo1.mostrar()
    circulo1.area()
    circulo1.circunferencia()
    circulo1.diametro()
    print("\n=== CIRCULO 2 ===")
    circulo2 = Circulo()
    circulo2.leer()
    circulo2.mostrar()
    circulo2.area()
    circulo2.circunferencia()
    circulo2.diametro()
main()