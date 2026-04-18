class Libro:
    # Lista interna (encapsulada) para guardar todos los libros
    lista_libros = []

    def __init__(self, titulo, autor, paginas, anio):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.anio = anio

    @staticmethod
    def registrar_n_libros(n):
        for i in range(n):
            print(f"\nLibro {i+1}:")
            t = input("Título: ")
            a = input("Autor: ")
            p = int(input("Número de páginas: "))
            y = int(input("Año de publicación: "))
            # Creamos el objeto y lo guardamos en la lista de la clase
            nuevo_libro = Libro(t, a, p, y)
            Libro.lista_libros.append(nuevo_libro)
        print(f"\n{n} libros registrados con éxito.")

    # --- MÉTODO ESTÁTICO 2: Mostrar N libros ---
    @staticmethod
    def mostrar_libros():
        if not Libro.lista_libros:
            print("No hay libros registrados.")
            return

        print("\n--- LISTA DE LIBROS ---")
        for libro in Libro.lista_libros:
            print(f"'{libro.titulo}' por {libro.autor} ({libro.anio}) - {libro.paginas} pág.")

    # --- MÉTODO ESTÁTICO 3: Consultas por año ---
    @staticmethod
    def consultar_por_anio(anio_limite):
        print(f"\nLibros publicados después del año {anio_limite}:")
        encontrados = False
        for libro in Libro.lista_libros:
            if libro.anio > anio_limite:
                print(f"- {libro.titulo} ({libro.anio})")
                encontrados = True
        if not encontrados:
            print("No se encontraron libros posteriores a ese año.")

    # --- MÉTODO ESTÁTICO 4: Búsqueda por autor ---
    @staticmethod
    def buscar_por_autor(nombre_autor):
        print(f"\nObras de {nombre_autor}:")
        encontrados = False
        for libro in Libro.lista_libros:
            if libro.autor.lower() == nombre_autor.lower():
                print(f"- {libro.titulo}")
                encontrados = True
        if not encontrados:
            print(f"No se encontraron obras de {nombre_autor}.")
    @staticmethod
    def menu():
        while True:
            print("\n" + "="*20)
            print("   MENÚ BIBLIOTECA")
            print("="*20)
            print("1. Registrar libros")
            print("2. Mostrar libros")
            print("3. Consultas (por año)")
            print("4. Búsqueda (por autor)")
            print("5. Salida")

            opcion = input("Elija una opción: ")

            if opcion == "1":
                n = int(input("¿Cuántos libros desea registrar?: "))
                Libro.registrar_n_libros(n)
            elif opcion == "2":
                Libro.mostrar_libros()
            elif opcion == "3":
                anio = int(input("Ingrese el año límite: "))
                Libro.consultar_por_anio(anio)
            elif opcion == "4":
                autor = input("Ingrese el nombre del autor: ")
                Libro.buscar_por_autor(autor)
            elif opcion == "5":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

# Arrancamos el programa
if __name__ == "__main__":
    Libro.menu()