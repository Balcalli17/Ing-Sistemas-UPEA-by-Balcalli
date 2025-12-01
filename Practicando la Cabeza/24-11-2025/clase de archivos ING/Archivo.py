"""
creamos un archivo de texto.
variable_archivo = open("nombre del archivo de texto ".txt" [extension]", "w")
.txt = es un ejemplo de extension que utilizamos para el ejemplo
"""
archivo = open("registro.txt","w") #"w" de write o escribir, y "open" de abrir

#una vez que ejecutamos, se crea en el gestor de archivos, un documento .txt
"""
escritura de datos en el archivo dentro de IDE:
variable_archivo.write("contenido")
"""
archivo.write("Lunes,")
archivo.write("Martes,")
archivo.write("Sabado,")

"""
para cerrar el archivo
variable_archivo.close()

OBS:si no lo colocas al fin de cada registro en el texto, toda la modificacion no se guardara
"""
archivo.close() #"close" de cerrar

"""
Añadir datos en el archivo de texto:
variable_archivo = open("nombre_del_archivo", "a")
"""
archivo = open("registro.txt", "a") #"a" de añadir o append
archivo.write("Miercoles,")
archivo.write("Jueves,")
archivo.write("Viernes")
archivo.close()
"""
leer la informacion del archivo:
variable_archivo = open("nombre_del_archivo.txt", "r")
"""
archivo = open("registro.txt", "r") #"r" de leer o read
print("contenido del archivo de texto")
print(archivo.readlines()) #"readlines" leer lineas 
archivo.close()
