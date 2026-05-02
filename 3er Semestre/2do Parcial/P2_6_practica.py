class Animal:
    def Comer(self):
        print("Comiendo...")

class Mamifero(Animal):
    def Amamantar(self):
        print("Tomando chuchu...")

class Ave(Animal):
    def Volar(self):
        print("Despegando...")

class Murcielago(Mamifero, Ave):
    pass

def main():
    pet = Murcielago()
    pet.Amamantar()
    pet.Volar()
    pet.Comer()
main()

#Despues explico como hacer...