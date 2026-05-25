class Empleado:
    def __init__(self, nombre, apellido, celular, salario):
        self.nombre   = nombre
        self.apellido = apellido
        self.celular  = celular
        self.salario  = salario

class Mensajero(Empleado):
    def registrar(self):
        print(f"Registrando mensajero: {self.nombre} {self.apellido}")
        print(f"  Celular: {self.celular} | Salario: Bs. {self.salario:.2f}")

    def mostrar(self):
        print(f"=== MENSAJERO ===")
        print(f"Nombre  : {self.nombre} {self.apellido}")
        print(f"Celular : {self.celular}")
        print(f"Salario : Bs. {self.salario:.2f}")

class Analista(Empleado):
    def __init__(self, nombre, apellido, celular, salario,
                 nombre_sistema_desarrollado, bono_produccion):
        super().__init__(nombre, apellido, celular, salario)
        self.nombre_sistema_desarrollado = nombre_sistema_desarrollado
        self.bono_produccion             = bono_produccion

    def actualizar_salario(self):
        return self.salario + self.bono_produccion

    def registrar(self):
        print(f"Registrando analista: {self.nombre} {self.apellido}")
        print(f"  Sistema: {self.nombre_sistema_desarrollado}")
        print(f"  Bono: Bs. {self.bono_produccion:.2f}")

    def mostrar(self):
        print(f"=== ANALISTA ===")
        print(f"Nombre   : {self.nombre} {self.apellido}")
        print(f"Celular  : {self.celular}")
        print(f"Sistema  : {self.nombre_sistema_desarrollado}")
        print(f"Salario actualizado: Bs. {self.actualizar_salario():.2f}")

# ── Programa principal ──
m = Mensajero("Pedro", "Quispe", "71234567", 3500)
a = Analista("María", "López", "78901234", 5000,
             "Sistema de Inventario", 800)

m.registrar()
m.mostrar()
print()
a.registrar()
a.mostrar()