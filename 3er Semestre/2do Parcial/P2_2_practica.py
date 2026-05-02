class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, nota, ru):
        super().__init__(nombre, edad, nacionalidad)
        self.nota = nota
        self.ru = ru 

    def toString(self):
        print(f"El estudiante {self.nombre} con edad de {self.edad} años, {self.nacionalidad}, con RU: {self.ru}, tiene la nota de {self.nota}")

def main():
    nombre = input("Ingrese el nombre del estudiante: ")
    edad = int(input("Ingrese la edad: "))
    nacional = input("Ingrese la nacionalidad: ")
    nota = int(input("Ingrese la nota del estudiante: "))
    ru = int(input("Ingrese el RU: "))
    objeto = Estudiante(nombre, edad, nacional, nota, ru)
    objeto.toString()
main()