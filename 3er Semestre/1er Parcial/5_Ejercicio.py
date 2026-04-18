class Rectangulo():
    def __init__(self, base, altura):
        self.set_base(base)
        self.set_altura(altura)
    
    def set_base(self, nueva_base):
        if nueva_base > 0:
            self._base = nueva_base
        else:
            self._base = 1
            print("Error: La base debe ser mayor a 0. Se asigno 1.")
    
    def set_altura(self, nueva_altura):
        if nueva_altura > 0:
            self._altura = nueva_altura
        else:
            self._altura = 1
            print("Error: La altura debe ser mayor a 0. Se asigno 1.")

    def get_base(self):
        return self._base
    
    def get_altura(self):
        return self._altura
    
    def calcular_area(self):
        return self._base * self._altura
    
    def calcular_perimetro(self):
        return 2 * (self._base + self._altura)
    
    def toString(self):
        return (f"RECTANGULO: [Base: {self._base}|Altura: {self._altura}|Area: {self.calcular_area()}|Perimetro: {self.calcular_perimetro()}]")
    
mi_rectangulo = Rectangulo(10, 5)
print(mi_rectangulo.toString())