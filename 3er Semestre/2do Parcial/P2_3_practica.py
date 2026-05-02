class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def mostrar(self):
        print("DATOS DEL PERSONAL")
        print(f"Nombre: {self.nombre}")
        print(f"Salario: {self.salario}")  

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.bono = bono

    def calcular(self):
        return self.salario + self.bono
    
def main():
    gerente1 = Gerente("Hugo", 2000, 120)
    gerente2 = Gerente("Juan", 2100, 160)
    if gerente1.calcular() > gerente2.calcular():
        gerente1.mostrar()
        print(f"{gerente1.nombre} gana mas que {gerente2.nombre}.")
    else:
        gerente2.mostrar()
        print(f"{gerente2.nombre} gana mas que {gerente1.nombre}.")
main()