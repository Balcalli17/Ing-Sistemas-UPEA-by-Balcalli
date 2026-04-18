class Estudiante:
    def __init__(self, nombre, edad, año_ingreso):
        self.nombre = nombre
        self.edad = edad
        self.año_ingreso = año_ingreso

    def mostrar_datos(self):
        print(f"El estudiante=> nombre: {self.nombre}, edad: {self.edad}, año del ingreso: {self.año_ingreso}.")

    def misma_edad(self, x):
        if self.edad == x.edad:
            return True
        else:
            return False
        
    def deteminar_mayor(self, x):
        if self.edad > x.edad:
            return print(f"El estudiante {self.nombre} es mayor que {x.nombre}.")
        elif x.edad > self.edad:
            return print(f"El estudiante {x.nombre} es mayor que {self.nombre}.")
        else:
            print("Los dos estudiantes tienen la misma edad.")

    def mismo_año(self, x):
        if self.año_ingreso == x.año_ingreso:
            return True
        else:
            return False
        
def main():
    nombre = input("Ingrese el nombre del 1er estudiante: ")
    edad = int(input("Ingrese su edad: "))
    año_ingreso = int(input("Ingrese el año de ingreso en la Universidad: "))
    est1=Estudiante(nombre, edad, año_ingreso)
    nombre = input("Ingrese el nombre del 2do estudiante: ")
    edad = int(input("Ingrese su edad: "))
    año_ingreso = int(input("Ingrese el año de ingreso en la Universidad: "))
    est2=Estudiante(nombre, edad, año_ingreso)
    print("\n===DATOS DE LOS ESTUDIANTES:===")
    est1.mostrar_datos()
    est2.mostrar_datos()
    print("\n===RESULTADOS:===")
    if est1.misma_edad(est2):
        print("Tienen la misma edad.")
    else:
        print("No tienen la misma edad.")
    est1.deteminar_mayor(est2)

    if est1.mismo_año(est2):
        print("Ingresaron el mismo año.")
    else:
        print("Ingresaron en diferentes años")
main()