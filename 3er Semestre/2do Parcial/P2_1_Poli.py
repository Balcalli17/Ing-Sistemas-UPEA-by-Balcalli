class Empleado:
    def __init__(self, nombre, id_empleado, salario_base):
        self.nombre        = nombre
        self.id_empleado   = id_empleado
        self.salario_base  = salario_base

    def presentarse(self):
        print(f"Empleado: {self.nombre} | ID: {self.id_empleado}")

    def calcular_salario_mensual(self):
        return self.salario_base

class Desarrollador(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, lenguaje_principal):
        super().__init__(nombre, id_empleado, salario_base)
        self.lenguaje_principal = lenguaje_principal

    def presentarse(self):
        print(f"Desarrollador: {self.nombre} | Lenguaje: {self.lenguaje_principal}")

    def calcular_salario_mensual(self):
        return self.salario_base * 1.15  # +15% por especialización

class Gerente(Empleado):
    def __init__(self, nombre, id_empleado, salario_base, departamento):
        super().__init__(nombre, id_empleado, salario_base)
        self.departamento = departamento

    def presentarse(self):
        print(f"Gerente: {self.nombre} | Depto: {self.departamento}")

    def calcular_salario_mensual(self):
        return self.salario_base * 1.30  # +30% por cargo gerencial

# ── Programa principal ──
emp  = Empleado("Carlos Mamani",   "EMP-001", 5000)
dev  = Desarrollador("Ana Flores", "DEV-002", 6000, "Python")
ger  = Gerente("Luis Quispe",      "GER-003", 8000, "Tecnología")

empleados = [emp, dev, ger]
print("=== SISTEMA DE EMPLEADOS ===")
for e in empleados:
    e.presentarse()
    print(f"  Salario mensual: Bs. {e.calcular_salario_mensual():.2f}")
    print()
