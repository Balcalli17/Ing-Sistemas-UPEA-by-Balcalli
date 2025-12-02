# FUNCIONES:
def crear_archivo():
    with open("empleados.txt", "w") as file:
        print("Archivo creado exitosamente...")

"""
Con el uso de "with", nos podemos ahorrar el uso anteriormente enseñado, como ser "file.open" y cerrarlo con "file.close",
ya que todo dentro de "with" si va a abrir el archivo, una vez ejecutado todo las operaciones realizadas, se cierra el
archivo por si solo.
"""

def insertar_datos():
    with open("empleados.txt", "a") as file:
        file.write("Ing.Emerson, 30, varon\n")
        file.write("Tec.Juan, 27, varon\n")
        file.write("Sra.Juana, 30, mujer\n")
        file.write("Lic.pepito, 30, varon\n")
        
def mostrar_datos():
    with open("empleados.txt", "r") as file:
        print("\nDATOS DE LOS EMPLEADOS:")
        print("===Nombre===,===Edad===,===Sexo===")
        contenido = file.read()
        print(contenido)
        
def mostrar_num_registros():
    with open("empleados.txt", "r") as file:
        numRegistros = len(file.readlines())
        print(f"\nEl numero de registros del archivo es {numRegistros}.")
        
# PROGRAMA PRINCIPAL:
def main():
    crear_archivo()
    insertar_datos()
    mostrar_datos()
    mostrar_num_registros()
main()
