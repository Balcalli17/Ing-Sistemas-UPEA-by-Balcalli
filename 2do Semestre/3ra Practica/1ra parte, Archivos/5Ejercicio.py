"""
5.Realice un programa para guardar y mostrar los datos de sus contactos en un archivo 
(contactos.csv o contactos.txt). El archivo debe contener: nombre, celular, separados por comas.
"""
#FUNCIONES:
def crearArchivo():
    with open("contactos.txt", "w") as file:
        print("Archivo creado/reiniciado exitosamente...")
        
def insertarArchivo():
    nombre = input("ingrese nombre: ")
    celular = input("ingrese numero celular: ")
        
    linea = f"{nombre},{celular}\n"
        
    with open("contactos.txt", "a") as file:
        file.write(linea)
    print()
        
    print("Datos registrado correctamente...")
    
def mostrarArchivo():
    with open("contactos.txt", "r") as file:
        print("\nDATOS DE LOS ESTUDIANTE:")
        contenido = file.read()
        print(contenido)
        
#PROGRAMA PRINCIPAL:
def main():
    while True:
        try:
            print("===MENU DE OPCIONES:===")
            print("1. Crear Archivo")
            print("2. Ingresar Datos")
            print("3. Mostrar Archivo")
            print("4. Salir")
            op = int(input("Ingrese numero: "))
            if op == 4:
                print("Saliendo...")
                break
            else:
                if op == 1:
                    crearArchivo()
                elif op == 2:
                    insertarArchivo()
                elif op == 3:
                    mostrarArchivo()
                else:
                    print("No existe este numero en opciones.")
        except ValueError:
            print("ingrese solamente numeros, y lo que se encuentre en el menu...")
main()
