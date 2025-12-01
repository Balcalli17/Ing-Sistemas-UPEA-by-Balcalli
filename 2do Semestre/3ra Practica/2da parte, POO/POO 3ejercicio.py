"""
3.Crear una clase "Rectángulo" con atributos descritos en el diagrama de clase. Debe implementar el constructor,
los métodos de leer, mostrar y los métodos que permitan calcular el área y perímetro del rectángulo.
"""
#FUNCIONES Y POO: 
class Rectangulo:
    def __init__(self,ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def leer(self):
        self.ancho = float(input("Ingrese el ancho del rectangulo:"))
        self.altura = float(input("Ingrese la altura del rectangulo: "))

    def mostrar(self):
        print(f"Ancho: {self.ancho}, Altura: {self.altura}.")
        
    def area(self):
        return self.ancho * self.altura
    def perimetro(self):
        return 2 * (self.ancho + self.altura)
    
#PROGRAMA PRINCIPAL:
def main():
    rectangulo = Rectangulo(0,0)
    rectangulo.leer()
    rectangulo.mostrar()
    print(f"El area del rectangulo es: {rectangulo.area()}")
    print(f"El perimetro del rectangulo es: {rectangulo.perimetro()}")
main()