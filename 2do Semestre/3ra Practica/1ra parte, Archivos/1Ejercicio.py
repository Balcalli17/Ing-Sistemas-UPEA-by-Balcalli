"""
1.Realiza un programa que pida el nombre de n personas y los almacene a un archivo denominado personas.txt.
Ejemplo:
Si n=5
en el archivo.txt., mostrar: Ana, Luis, Marta, Carlos y Elena
"""
#FUNCIONES: 
def crear_archivo():
    file = open("personas.txt", "w") 
    file.close()
    print("Archivo 'personas.txt' creado/reiniciado correctamente.")

def pedir_y_guardar():
    file = open("personas.txt", "a")    
    n = int(input("¿Cuántas personas deseas registrar?: "))

    for i in range(n):
        nombre = input(f"Ingresa el nombre de la persona {i+1}: ")
        # Escribimos el nombre y añadimos "\n" para que haga un salto de línea
        file.write(nombre + "\n")

    file.close()
    print("Nombres guardados exitosamente.")

def mostrar_archivo():
    file = open("personas.txt", "r")
    contenido = file.read()
    print("\n--- CONTENIDO DEL ARCHIVO ---")
    print(contenido)
    file.close()

#PRINCIPAL:
def main():
    crear_archivo() 
    pedir_y_guardar() 
    mostrar_archivo() 
main()