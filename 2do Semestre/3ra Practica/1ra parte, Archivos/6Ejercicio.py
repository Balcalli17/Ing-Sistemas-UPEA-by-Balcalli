"""
6.Escribir un programa en Python que gestione un archivo de texto (productos.txt o productos.csv). 
Cada línea del archivo debe representar un producto con los siguientes campos separados por comas: 
nombre, precio, cantidad. El programa debe permitir leer el archivo, mostrar todos los productos y calcular 
el valor total del inventario (Precio * cantidad).
"""
#FUNCIONES:
def creararchivo():
    with open("productos.txt", "w")as file:
        print("Archivo creado/reiniciado correctamente...")

def insertararchivo():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    
    linea = f"{nombre},{precio},{cantidad}\n"
    
    with open("productos.txt", "a")as file:
        file.write(linea)
    print()
    
    print("Datos registrado correctamente...")

def mostrararchivo():
    with open("productos.txt", "r")as file:
        print("\nDATOS DE LOS PRODUCTOS:")
        contenido = file.read()
        print(contenido)

def calcularinventario():
    total_inventario = 0.0
    with open("productos.txt", "r")as file:
        for linea in file:
            nombre, precio, cantidad = linea.strip().split(",")
            total_inventario += float(precio) * int(cantidad)
    print(f"\nEl valor total del inventario es: ${total_inventario:.2f}")

#PRINCIPAL:
def main():
    while True:
        try:
            print("\nMENU DE OPCIONES:")
            print("1. Crear/Reiniciar archivo")
            print("2. Insertar producto")
            print("3. Mostrar productos")
            print("4. Calcular valor total del inventario")
            print("5. Salir")
            opcion = int(input("Seleccione una opcion (1-5): "))
            if opcion == 1:
                creararchivo()
            elif opcion == 2:
                insertararchivo()
            elif opcion == 3:
                mostrararchivo()
            elif opcion == 4:
                calcularinventario()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opcion no valida. Intente de nuevo.")
        except ValueError:
            print("Entrada invalida. Por favor, ingrese un numero.")
main()