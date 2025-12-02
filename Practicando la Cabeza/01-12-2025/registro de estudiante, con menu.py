#FUNCIONES:
def crearArchivo():
    with open("registu.txt", "w") as study:
        print("Archivo creado exitosamente...")
        
def insertarArchivo():
    nombre = input("ingrese nombre: ")
    ci = input("ingrese CI: ")
    nota = input("ingrese Nota: ")
        
    linea = f"{nombre},{ci},{nota}\n"
        
    with open("registu.txt", "a") as study:
        study.write(linea)
    print()
        
    print("Datos registrado correctamente...")
    
def mostrarArchivo():
    with open("registu.txt", "r") as study:
        print("\nDATOS DE LOS ESTUDIANTE:")
        contenido = study.read()
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