"""
3.Realiza un programa que dado un archivo de texto (.txt), muestre un resumen:
a)Cantidad de líneas
b)Cantidad total de palabras
c)Cantidad total de caracteres
Realiza un programa que dado un archivo de texto (.txt), muestre la cantidad de veces que se repite
una palabra x, introducida desde teclado.
"""
#FUNCIONES:
def analizar_documento():
    nombre_archivo = input("Introduce el nombre del archivo a leer: ")
    try:
        with open(nombre_archivo, "r") as file:
            contenido = file.read()
            # 1.Contamos caracteres (letras, espacios, puntos)
            cant_caracteres = len(contenido)
            # 2.Contamos palabras (usamos split para separar por espacios)
            lista_palabras = contenido.split()
            cant_palabras = len(lista_palabras)
            # 3.Contamos líneas (usamos split para separar por 'Enter')
            lista_lineas = contenido.split("\n")
            cant_lineas = len(lista_lineas)
            print(f"\n--- RESUMEN DE {nombre_archivo} ---")
            print(f"Total de líneas: {cant_lineas}")
            print(f"Total de palabras: {cant_palabras}")
            print(f"Total de caracteres: {cant_caracteres}")
            # 4.Contamos repeticiones de una palabra dada
            palabra_buscada = input("\n¿Qué palabra quieres contar?: ")
            contador = 0
            
            for palabra in lista_palabras:
                if palabra.lower() == palabra_buscada.lower():
                    contador += 1
            
            print(f"La palabra '{palabra_buscada}' se repite {contador} veces.")
            
    except FileNotFoundError:
        print("Error: No encontré ese archivo. Asegúrate de crearlo primero.")
#PRINCIPAL:
analizar_documento()