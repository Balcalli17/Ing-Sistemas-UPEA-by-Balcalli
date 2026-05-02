"""
crea uma clase animal con el atributo nombre y un metodo comer() y una clase perro que
herede de animal y añada 
"""
class Animal():
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        print("Yummi yummi, buen provecho.")

class Perro(Animal):
    def ladrar(self):
        print(f"El perrito {self.nombre} ladra, Guau Guau!!!.")

def main():
    nombre = input("Cual es el nombre del perro: ")
    objeto = Perro(nombre)
    objeto.ladrar()
    objeto.comer()
main()