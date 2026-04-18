class Reloj:
    def __init__(self, hora, minutos, segundos):
        if 0 <= hora <= 23:
            self.hora=hora
        else:
            self.hora=0
            print("Hora inválida, se asignó 0")
        if 0 <= minutos <=59:
            self.minutos=minutos
        else:
            self.minutos=0
            print("Minuto inválido, se asignó 0")
        if 0 <= segundos <=59:
            self.segundos=segundos
        else:
            self.segundos=0
            print("Segundos inválidos, se asignó 0")

    def avanzar_segundo(self):
        self.segundos = self.segundos + 1
        if self.segundos == 60:
            self.segundos = 0
            self.minutos = self.minutos + 1
            if self.minutos == 60:
                self.minutos = 0
                self.hora = self.hora + 1
                if self.hora == 24:
                    self.hora = 0

    def retroceder_segundo(self):
        self.segundos = self.segundos - 1
        if self.segundos < 0:
            self.segundos = 59
            self.minutos = self.minutos - 1
            if self.minutos < 0:
                self.minutos = 59
                self.hora = self.hora - 1
                if self.hora < 0:
                    self.hora = 23

    def mostrar_hora(self):
        print(f"{self.hora:02d}:{self.minutos:02d}:{self.segundos:02d}")

mi_reloj=Reloj(23,59,59)

print("Hora Inicial: ")
mi_reloj.mostrar_hora()

mi_reloj.avanzar_segundo()
print("Avanzo 1 segundo")
mi_reloj.mostrar_hora()

mi_reloj.retroceder_segundo()
print("Retrocedio 1 segundo")
mi_reloj.mostrar_hora()