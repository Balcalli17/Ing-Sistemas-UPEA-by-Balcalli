"""
10.
Cree el archivo de texto (amigos.txt o amigos.csv), en el que almacene la información del nombre, edad, lugar de nacimiento, separados por comas. Por ejemplo:
Realice las siguientes funciones:
•Creación del archivo
•Guardar en archivo
•Leer el archivo
•Mostrar todos los nacidos en un lugar x.
•Contar cuántos jóvenes tienen entre 13 a 17 años
"""
#FUNCIONES:
def creararchivo():
    with open("amigos.txt", "w") as file:
        print("Archivo creado/reiniciado exitosamente...")

def insertardatos():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    lugar_nacimiento = input("Ingrese el lugar de nacimiento (departamente): ")
    
    linea = f"{nombre},{edad},{lugar_nacimiento}\n"
    
    with open("amigos.txt", "a") as file:
        file.write(linea)
    print()
    
    print("Datos registrado correctamente...")

def mostrararchivo():
    with open("amigos.txt", "r") as file:
        print("\nDATOS DE LOS AMIGOS:")
        contenido = file.read()
        print(contenido)

def nacidos_en_lugar(lugar):
    with open("amigos.txt", "r") as file:
        amigos = file.readlines()
        
    print(f"\nAmigos nacidos en {lugar}:")
    for amigo in amigos:
        nombre, edad, lugar_nacimiento = amigo.strip().split(",")
        if lugar_nacimiento.lower() == lugar.lower():
            print(f"- {nombre}, Edad: {edad}")

def contar_jovenes():
    with open("amigos.txt", "r") as file:
        amigos = file.readlines()
        
    contador = 0
    for amigo in amigos:
        nombre, edad, lugar_nacimiento = amigo.strip().split(",")
        if 13 <= int(edad) >= 17:
            contador += 1
            
    print(f"\nCantidad de jóvenes entre 13 y 17 años: {contador}")

#PRINCIPAL:
def main():
    creararchivo()
    
    while True:
        print("\nMenú:")
        print("1. Insertar datos de un amigo")
        print("2. Mostrar todos los amigos")
        print("3. Mostrar amigos nacidos en un lugar específico")
        print("4. Contar jóvenes entre 13 y 17 años")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            insertardatos()
        elif opcion == "2":
            mostrararchivo()
        elif opcion == "3":
            lugar = input("Ingrese el lugar de nacimiento a buscar: ")
            nacidos_en_lugar(lugar)
        elif opcion == "4":
            contar_jovenes()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
main()
