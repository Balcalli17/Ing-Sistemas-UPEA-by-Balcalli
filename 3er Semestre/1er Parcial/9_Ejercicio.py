class Celular:

    def __init__(self,i,m,c,p):
        self.__imei = i
        self._marca = m
        self.color = c
        self.precio = p

    #getters
    def getIMEI(self):
        return self.__imei

    #setters
    def setIMEI(self,nuevo_imei):
        self.__imei = nuevo_imei
        return self.__imei

    def mostrar_datos(self):
        print("----------------------------------")
        print(f"Imei:{self.__imei}")
        print(f"Marca: {self._marca}")
        print(f"Color:{self.color}")
        print(f"Precio:{self.precio}")

objeto = Celular(665465,"Nokia","Negro",500)
objeto.mostrar_datos()

objeto.__imei=88888

objeto.mostrar_datos()