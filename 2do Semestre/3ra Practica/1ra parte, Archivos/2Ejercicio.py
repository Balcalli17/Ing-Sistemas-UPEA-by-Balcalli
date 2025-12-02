"""
2.Realiza un programa que permita abrir y mostrar todo el contenido de cualquier archivo de texto (.txt).
Por ejemplo:
    Del anterior ejercicio, abrir el archivo "personas.txt" y mostrar su contenido.
"""
#FUNCIONES:
def abrir_y_mostrar():
    nombre_archivo = input("Introduce el nombre del archivo a abrir (ej: personas.txt): ")
    
    try:
        file = open(nombre_archivo, "r")
        
        contenido = file.read()
        print(f"\n--- MOSTRANDO CONTENIDO DE: {nombre_archivo} ---")
        print(contenido)
        
        file.close()
        
    except FileNotFoundError:
        # Esto es un control de errores por si el usuario escribe mal el nombre
        print(f"Error: El archivo '{nombre_archivo}' no existe.")

#PRINCIPAL:
def main():
    abrir_y_mostrar()
main()