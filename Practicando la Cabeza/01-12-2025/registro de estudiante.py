def crearArchivo():
    with open("registu.txt", "w") as study:
        print("Archivo creado exitosamente...")
        
def insertarArchivo():
    num = int(input("ingrese la cantidad de estudiantes: "))
    for i in range(num):
        nombre = input("ingrese nombre: ")
        ci = input("ingrese CI: ")
        nota = input("ingrese Nota: ")
        
        linea = f"{nombre},{ci},{nota}\n"
        
        with open("registu.txt", "a") as study:
            study.write(linea)
        print()
        
def mostrarArchivo():
    with open("registu.txt", "r") as study:
        print("\nDATOS DE LOS ESTUDIANTE:")
        contenido = study.read()
        print(contenido)
        
def main():
    crearArchivo()
    insertarArchivo()
    mostrarArchivo()
main()
        