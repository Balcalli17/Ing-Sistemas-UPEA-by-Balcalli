#FUNCIONES
def crear_archivo():
    file = open("estudiantes.txt", "w")
    file.close()

def llenar_datos():
    file = open("estudiantes.txt", "a")
    file.write("Guido Amigo, Varon, 26 años \n")
    file.write("Ima Amigo, Varon, 15 años \n")
    file.write("Rafa Amigo, Varon, 23 años \n")
    file.write("Emer Amigo, Varon, 24 años \n")
    file.close()

def mostrar_datos():
    file = open("estudiantes.txt", "r")
    print("DATOS DE LOS ESTUDIANTES: ")
    contenido = file.read()
    print(contenido)
    lineas = contenido.split("\n") #"split" significa dividir o separar
    print(lineas)
    file.close()
    
#PROGRAMA PRINCIPAL
def main():
    crear_archivo()
    llenar_datos()
    mostrar_datos()
main()