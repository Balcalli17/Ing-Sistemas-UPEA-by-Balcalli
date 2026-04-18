class Curso:
    def __init__(self,nombre,instructor,fecha,lugar,hora,costo):
        self.nombre = str(nombre)
        self.instructor = str(instructor)
        self.fecha = str(fecha)
        self.lugar = str(lugar)
        self.hora = str(hora)
        self.costo = float(costo)

    @classmethod  # constructor alternativo
    def crear_clase(cls,nombre,instructor,fecha,lugar,hora,costo):
        return cls(nombre,instructor,fecha,lugar,hora,costo)

    def mostrar_datos(self):
        print(f"Curso:{self.nombre}")

    def lista_curso(self):
        return self.nombre

curso1 = Curso("Python","Jose","10-10-2026","La Paz","08:05:50",45)
curso2 = Curso.crear_clase("Java","Pepe","10-10-2026","La Paz","08:05:50",45)

lista = [curso1.lista_curso(),curso2.lista_curso()]

