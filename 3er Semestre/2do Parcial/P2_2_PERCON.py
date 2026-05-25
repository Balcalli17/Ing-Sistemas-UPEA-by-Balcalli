import pickle

class Libro:
    def __init__(self, codigo, titulo, autor, anio_edicion):
        self.codigo       = codigo
        self.titulo       = titulo
        self.autor        = autor
        self.anio_edicion = anio_edicion

    def __str__(self):
        return (f"Código: {self.codigo} | Título: {self.titulo} | "
                f"Autor: {self.autor} | Año: {self.anio_edicion}")

class Biblioteca:
    def __init__(self, nombre_de_archivo):
        self.nombre_de_archivo = nombre_de_archivo

    def guardar(self, libros):
        with open(self.nombre_de_archivo, 'wb') as f:
            pickle.dump(libros, f)
        print(f"Biblioteca guardada en '{self.nombre_de_archivo}'.")

    def mostrar(self):
        try:
            with open(self.nombre_de_archivo, 'rb') as f:
                libros = pickle.load(f)
            print("\n=== CATÁLOGO DE LIBROS ===")
            for lb in libros:
                print(f"  {lb}")
        except FileNotFoundError:
            print("Archivo no encontrado.")

    def buscar(self, codigo_buscado):
        try:
            with open(self.nombre_de_archivo, 'rb') as f:
                libros = pickle.load(f)
            for lb in libros:
                if lb.codigo == codigo_buscado:
                    print(f"\nLibro encontrado: {lb}")
                    return
            print(f"No se encontró libro con código '{codigo_buscado}'.")
        except FileNotFoundError:
            print("Archivo no encontrado.")

# ── Programa principal ──
bib = Biblioteca("biblioteca.pkl")

n = int(input("¿Cuántos libros registrar? "))
libros = []
for i in range(n):
    print(f"\n-- Libro {i+1} --")
    cod  = input("Código        : ")
    tit  = input("Título        : ")
    aut  = input("Autor         : ")
    anio = int(input("Año de edición: "))
    libros.append(Libro(cod, tit, aut, anio))

bib.guardar(libros)
bib.mostrar()

cod_buscar = input("\nIngrese código a buscar: ")
bib.buscar(cod_buscar)
