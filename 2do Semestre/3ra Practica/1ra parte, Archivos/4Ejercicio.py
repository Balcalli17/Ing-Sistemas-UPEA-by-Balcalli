"""
4.Realiza un programa que realice una copia de un archivo (txt). Primeramente, pida al usuario el nombre del
archivo, luego realice la lectura del contenido y escriba en un nuevo archivo. (Sin usar la librería os).
"""
#FUNCIONES:
def realizar_copia():
    print("--- COPIADOR DE ARCHIVOS ---")
    origen = input("Nombre del archivo original (ej: texto_prueba.txt): ")
    try:
        #1.LEER: Abrimos el original con 'r'
        with open(origen, "r") as file_origen:
            datos = file_origen.read() # Guardamos todo en la variable 'datos'
        
        #2.ESCRIBIR: Pedimos nombre para la copia y abrimos con 'w'
        destino = input("Nombre para la copia (ej: copia_texto.txt): ")
        
        with open(destino, "w") as file_destino:
            file_destino.write(datos) # Escribimos lo que leímos antes
            
        print(f"¡Listo! Se ha creado el archivo '{destino}' correctamente.")
        
    except FileNotFoundError:
        print(f"Error: El archivo '{origen}' no existe.")
#PRINCIPAL:
realizar_copia()