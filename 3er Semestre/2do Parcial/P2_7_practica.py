class Animal:
    def __init__(self, habitad):
        self.habitad = habitad

class Terrestre(Animal):
    def mostrar(self):
        print(f"Habitad: {self.habitad}")

class Acuatico(Animal):
    def mostrar(self):
        print(f"Habitad: {self.habitad}")

class Anfibio(Terrestre, Acuatico):
    def __init__(self, habitad, tipo):
        super().__init__(habitad)
        self.tipo = tipo
    
    def mostrar(self):
        print("DATOS DEL ANIMAL:")
        print(f"Tipo: {self.tipo}")
        super().mostrar()
        
def main():
    pet = Anfibio("Tierra - Agua", "Rana")
    pet.mostrar()
main()

#Despues explico como hacer...