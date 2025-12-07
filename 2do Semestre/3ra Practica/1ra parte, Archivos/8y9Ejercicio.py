"""
8.Crear un programa para registrar asistencia de estudiantes (asistencia.txt o asistencia.csv), el programa debe registrar la asistencia 
tomado los datos: fecha,nombre,ci.
9.Dado un CI, introducido por teclado, el programa debe mostrar las fechas en la que asistió el estudiante.
Por ejemplo:
Si  CI=90123541

2025-11-20 Juan
2025-11-21 Juan
2025-11-22 Juan
3 asistencias
"""
#FUNCIONES:
def creararchivo():
    with open("asistencia.txt", "w")as file:
        print("Archivo creado/reiniciado exitosamente...")

def insertararchivo():
    fecha=input("Ingrese la fecha (dd/mm/aaaa): ")
    nombre=input("Ingrese el nombre del estudiante: ")
    ci=input("Ingrese la cedula de identidad: ")
    linea=f"{fecha},{nombre},{ci}\n"
    with open("asistencia.txt", "a")as file:
        file.write(linea)
    print()
    print("Datos registrado correctamente...")

def mostrararchivo():
    with open("asistencia.txt", "r")as file:
        print("\nDATOS DE ASISTENCIA:")
        contenido=file.read()
        print(contenido)

def contar_asistencias_por_ci():
    print("--- CONSULTAR ASISTENCIA ---")
    ci_buscado = input("Ingrese el CI a buscar: ")
    contador = 0
    
    try:
        with open("asistencia.txt", "r") as file:
            print(f"Fechas encontradas para el CI {ci_buscado}:")
            
            for linea in file:
                datos = linea.strip().split(',')
                # Formato: Fecha(0), Nombre(1), CI(2)
                if len(datos) == 3:
                    ci_actual = datos[2]
                    fecha = datos[0]
                    nombre = datos[1]
                    
                    if ci_actual == ci_buscado:
                        print(f"* {fecha} - {nombre}")
                        contador += 1
            
            print(f"Total de asistencias: {contador}")
            
    except FileNotFoundError:
        print("No hay archivo de asistencias creado aún.")
#PRINCIPAL:
def main():
    while True:
        try:
            print("\n--- MENU DE ASISTENCIA DE ESTUDIANTES ---")
            print("1. Crear/Reiniciar archivo de asistencia")
            print("2. Insertar registro de asistencia")
            print("3. Mostrar todos los registros de asistencia")
            print("4. Consultar asistencias por CI")
            print("5. Salir")
            opcion = int(input("Seleccione una opción (1-5): "))
            
            if opcion == 1:
                creararchivo()
            elif opcion == 2:
                insertararchivo()
            elif opcion == 3:
                mostrararchivo()
            elif opcion == 4:
                contar_asistencias_por_ci()
            elif opcion == 5:
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
main()