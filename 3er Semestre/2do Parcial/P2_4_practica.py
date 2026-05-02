class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrancar(self):
        print("Enciende el auto, raaammm, raaammm.\n")

class Npuertas(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.puertas = puertas

    def detalle(self):
        print("DATOS DEL VEHICULO:")
        print(f"El coche {self.marca}, modelo {self.modelo} tiene {self.puertas} puertas.")

def main():
    auto = Npuertas("Toyota", "Corolla", 4)
    auto.arrancar()
    auto.detalle()
main()
