"""
7.Escribir un programa en Python que abra un archivo (pacientes.txt o pacientes.csv), cuyo contenido es una lista de pacientes con los 
campos: CI, Nombre, Edad, Diagnóstico separados por comas. El programa debe permitir buscar un paciente por nombre y mostrar sus datos.
"""
#FUNCIONES:
def creararchivo():
    with open("pacientes.txt", "w") as file:
        print("Archivo creado/reiniciado exitosamente...")

def insertardatos():
    nombre = input("Ingrese el nombre del paciente: ")
    ci = input("Ingrese la CI del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    diagnostico = input("Ingrese el diagnóstico del paciente: ")
    
    linea = f"{ci},{nombre},{edad},{diagnostico}\n"
    
    with open("pacientes.txt", "a") as file:
        file.write(linea)
    print()
    
    print("Datos registrado correctamente...")

def buscarpaciente():
    nombre_buscar = input("Ingrese el nombre del paciente a buscar: ")
    encontrado = False
    
    with open("pacientes.txt", "r") as file:
        for linea in file:
            ci, nombre, edad, diagnostico = linea.strip().split(",")
            if nombre.lower() == nombre_buscar.lower():
                print(f"CI: {ci}, Nombre: {nombre}, Edad: {edad}, Diagnóstico: {diagnostico}")
                encontrado = True
                break
    
    if not encontrado:
        print("Paciente no encontrado.")

#PRINCIPAL:
def main():
    while True:
        try:
            print("\n--- Menú de Opciones ---")
            print("1. Crear/Reiniciar archivo de pacientes")
            print("2. Insertar datos de paciente")
            print("3. Buscar paciente por nombre")
            print("4. Salir")
            
            opcion = int(input("Seleccione una opción (1-4): "))
            
            if opcion == 1:
                creararchivo()
            elif opcion == 2:
                insertardatos()
            elif opcion == 3:
                buscarpaciente()
            elif opcion == 4:
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
main()
