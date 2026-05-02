class Telefono():
    def hacerLlamada(self):
        print("Llamando...")

class ReproductorMusica():
    def reproducirMusica(self):
        print("Reproduciendo musica...")

class SmartPhone(Telefono, ReproductorMusica):
    def __init__(self):
        pass

    def usarApps(self):
        print("Abriendo Mobile Legends...")

def main():
    objeto = SmartPhone()
    objeto.hacerLlamada()
    objeto.reproducirMusica()
    objeto.usarApps()
main()

#Despues explico como hacer...
