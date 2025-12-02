"""
Los principios de POO (Programacion orientada a objetos)
la "class" en si, es crear un molde, una plantilla.
"""
#FUNCIONES Y CLASES:
#Almacenar los datos de un celular
#primero, definimos la clase
class Celular:
#creamos un constructor, al cual se representa como "def __init__", y dentro del "def", siempre va a entrar "self"
    def __init__(self, marca, modelo, camara):
        self.marc = marca
        self.mod = modelo
        self.cam = camara
#leer los datos
    def leer(self):
        self.marc = input("ingrese la marca del celular: ")
        self.mod = input("ingrese el modelo del celular: ")
        self.cam = input("ingrese el tipo de camara del celular: ")
#mostramos los datos
    def mostrar(self):
        print("DATOS DEL CELULAR")
        print(f"Marca: {self.marc}")
        print(f"Modelo: {self.mod}")
        print(f"Camara: {self.cam}")
#PRINCIPAL:
def main():
#Creamos un Objeto
    telefono = Celular("Samsung", "S24", "60MP")
    telefono2 = Celular("Samsung", "S24", "60MP")
#Leer los datos del objeto "telefono"
    telefono.leer()
    telefono2.leer()
#Mostrar los datos del objeto "telefono"
    telefono.mostrar()
    telefono2.mostrar()
main()