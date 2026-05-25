import pickle

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre   = nombre
        self.precio   = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"{self.nombre} | Bs. {self.precio:.2f} | Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self, nombre_de_archivo):
        self.nombre_de_archivo = nombre_de_archivo

    def guardar_archivo(self, productos):
        with open(self.nombre_de_archivo, 'wb') as f:
            pickle.dump(productos, f)
        print(f"Inventario guardado en '{self.nombre_de_archivo}'.")

    def leer_archivo(self):
        try:
            with open(self.nombre_de_archivo, 'rb') as f:
                productos = pickle.load(f)
            print(f"\n=== INVENTARIO ({self.nombre_de_archivo}) ===")
            for p in productos:
                print(f"  {p}")
        except FileNotFoundError:
            print("Archivo no encontrado.")

# ── Programa principal ──
inv = Inventario("inventario.pkl")

n = int(input("¿Cuántos productos registrar? "))
productos = []
for i in range(n):
    print(f"\n-- Producto {i+1} --")
    nom  = input("Nombre   : ")
    pre  = float(input("Precio   : "))
    cant = int(input("Cantidad : "))
    productos.append(Producto(nom, pre, cant))

inv.guardar_archivo(productos)
inv.leer_archivo()
