import os
#emerson balboa
archivo = "registro de datos.txt"

def creararchivo():
    if not os.path.exists(archivo):
        with open(archivo, "w") as file:
            pass
        print("archivo creado...")
    else:
        print("el archivo existe, ingrese otro nombre...")

def guardarregistro():
    print("ingrese los datos de los estudiante: ")
    ru = input("RU: ")
    ci = input("CI : ")
    apellido = input("apellido: ")
    nombre = input("nombre: ")
    sexo = input("sexo: ")
    nota=input("nota: ")

    linea= f"{ru},{ci},{apellido},{nombre},{sexo},{nota}"
    with open(archivo, "a") as file:
        file.write(linea)
    
    print("registrado correctamente...")
def cargardatosvec():
    estudiante = []
    if not os.path.exists(archivo):
        return  estudiante
    
    with open(archivo, "r") as file:
        for linea in file:
            partes = linea.strip().split(",")
            if len(partes) == 6:
                estudiante.append(partes)
    return estudiante

def mostrar():
    estudiantes = cargardatosvec()
    print("\n lista de estudiante ")
    for e in (estudiantes):
        print(e)
    print()

def modificar():
    estudiantes = cargardatosvec()
    ru = input("ingrese RU por modificar: ")
    encontrado = False

    for i in range(len(estudiantes)):
        if estudiantes[i][0] == ru:
            print("datos actuales del estudiante: ", estudiantes[i])
            estudiantes[i][2] = input("ingrese nuevo apellido: ")
            estudiantes[i][3] = input("ingrese nuevo nombre: ")
            estudiantes[i][4] = input("ingrese nuevo sexo: ")
            estudiantes[i][5] = input("ingrese nuevo nota: ")
            encontrado = True
            break

    if encontrado == True:
        with open(archivo, "w"):
            for e in estudiantes:
                archivo.write(",".join(e)+ "\n")
            print("registro modificado correctamente...")
    else:
        print("RU no encontrado...")

def menu():
    while True:
        print("\n ====== MENU PRINCIPAL: ======")
        print("1. crear archivo")
        print("2. guardar archivo")
        print("3. mostrar archivo")
        print("4. modificar archivo")
        print("0. salir.")
        opcion = input("ingrese una opcion:")
        if opcion == "1": creararchivo()
        elif opcion == "2": guardarregistro()
        elif opcion == "3": mostrar()
        elif opcion == "4": modificar()
        elif opcion == "0":
            print("saliendo del programa...")
        else:
            print("opcion no valida...")
menu()