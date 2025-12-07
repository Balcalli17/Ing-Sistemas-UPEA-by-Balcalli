"""
11.Crear un programa que permita al usuario almacenar los datos de personas: apellido,nombre,sexo. Los datos de
cada persona se deben guardar en una línea separados por comas.
ejemplo:
Mamani,José,M
Rojas,Isabela,F
Huanca,Flora ,F

En base al archivo de personas, generar 2 archivos: “varones.txt” y “mujeres.txt”. En cada archivo se deben
copiar los datos correspondientes, respectivamente.
"""
#FUNCIONES:
def registrar_personas():
    print("--- PASO 1: REGISTRO DE PERSONAS ---")
    # Abrimos en modo 'a' (append) para añadir sin borrar lo anterior
    with open("personas.txt", "a") as file:
        cantidad = int(input("¿Cuántas personas deseas registrar?: "))
        
        for i in range(cantidad):
            print(f"\nPersona #{i+1}:")
            apellido = input("Apellido: ")
            nombre = input("Nombre: ")
            # Pedimos M o F. Usamos .upper() para que se guarde mayúscula siempre
            sexo = input("Sexo (M=Masculino, F=Femenino): ").upper()
            
            # Guardamos separado por comas: Apellido,Nombre,Sexo
            linea = f"{apellido},{nombre},{sexo}\n"
            file.write(linea)
            
    print(">> Datos guardados en 'personas.txt'.")

def generar_archivos_clasificados():
    print("\n--- PASO 2: GENERANDO ARCHIVOS SEPARADOS ---")
    
    try:
        # 1. Abrimos el archivo origen para LEER ('r')
        with open("personas.txt", "r") as archivo_origen:
            # Leemos todas las líneas y las guardamos en una lista
            lista_completa = archivo_origen.readlines()

        # 2. Abrimos los dos archivos destino para ESCRIBIR ('w')
        # Usamos 'w' para que se creen limpios cada vez que clasificamos
        file_varones = open("varones.txt", "w")
        file_mujeres = open("mujeres.txt", "w")

        # 3. Recorremos la lista y repartimos
        count_v = 0
        count_m = 0

        for linea in lista_completa:
            # Quitamos espacios extra y separamos por comas
            # linea.strip().split(',') crea una lista: ['Mamani', 'Jose', 'M']
            datos = linea.strip().split(',')
            
            # Verificamos que la línea tenga los 3 datos para evitar errores
            if len(datos) == 3:
                sexo_persona = datos[2].strip() # El sexo está en la posición 2 (0, 1, 2)
                
                if sexo_persona == 'M':
                    file_varones.write(linea)
                    count_v += 1
                elif sexo_persona == 'F':
                    file_mujeres.write(linea)
                    count_m += 1

        # Importante: Cerrar los archivos que abrimos manualmente
        file_varones.close()
        file_mujeres.close()
        
        print(f">> Proceso terminado.")
        print(f"   - Se guardaron {count_v} registros en 'varones.txt'")
        print(f"   - Se guardaron {count_m} registros en 'mujeres.txt'")

    except FileNotFoundError:
        print("Error: Primero debes registrar personas (El archivo 'personas.txt' no existe).")

#PRINCIPAL:
def main():
    # Primero registramos unos cuantos datos
    registrar_personas()
    
    # Luego ejecutamos la clasificación
    generar_archivos_clasificados()
main()