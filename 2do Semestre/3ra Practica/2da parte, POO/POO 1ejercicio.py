#FUNCIONES Y POO
class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = ""
        
    def leer(self):
        self.nombre = input("ingrese el nombre: ")
        self.edad = input("ingrese la edad: ")
        
    def mostrar(self):
        print("MOSTRANDO DATOS:")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        
    def saludar(self):
        print(f"Buenos dias, soy {self.nombre} y tengo {self.edad} años.")
#PRINCIPAL:
def main():
    persona = Persona()
    persona.leer()
    persona.mostrar()
    persona.saludar()
main()