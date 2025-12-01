"""
2.Crear una clase "Estudiante" con atributos descritos en el diagrama de clase. Debe implementar el constructor,
los métodos de leer, mostrar y un método que permita cambiar (actualizar) el estado Activo/Retirado, del estudiante.
"""
#FUNCIONES Y POO: 
class Estudiante:
    def __init__(self):
        self.ci = 0
        self.ru= 0
        self.apellido = ""
        self.nombre = ""
        self.estado = ""

    def leer(self):
        self.ci = int(input("ingrese su CI: "))
        self.ru = int(input("ingrese su RU: "))
        self.apellido = input("ingrese su apellido: ")
        self.nombre = input("ingrese su nombre: ")
        self.estado = input("ingrese su estado (activo/retirado): ")

    def mostrar(self):
        print(f"CI: {self.ci}")
        print(f"RU: {self.ru}")
        print(f"Apellido: {self.apellido}")
        print(f"Nombre: {self.nombre}")
        print(f"Estado: {self.estado}")

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
#PRINCIPAL:
def main():
    Estudiante1 = Estudiante()
    Estudiante1.leer()
    Estudiante1.mostrar()
    Estudiante1.cambiar_estado("Retirado")
    Estudiante1.mostrar()
main()


