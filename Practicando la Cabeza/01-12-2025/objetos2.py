class Auto:
    def __init__(self, placa, marca, modelo, color):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def leer(self):
        self.placa = input("ingrese la placa del veiculo (Ej: 1234-abc): ")
        self.marca = input("ingrese la marca del veiculo: ")
        self.modelo = input("ingrese el modelo del veiculo (Ej: de que año es, 1999): ")
        self.color = input("ingrese el color del veiculo: ")
    
    def mostrar(self):
        print(f"Placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Color: {self.color}")

def main():
    carro = Auto("4745-PLC","Toyota","2015","azul")
    carro.leer()
    carro.mostrar()
main()