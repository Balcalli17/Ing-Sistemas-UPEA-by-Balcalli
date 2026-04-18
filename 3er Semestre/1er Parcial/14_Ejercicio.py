class Fraccion:
  
    def __init__(self, numerador, denominador):
        if denominador == 0:
            print("Error: El denominador no puede ser cero.")
        
        self.numerador = numerador
        self.denominador = denominador
        print(f"Fraccion {self.numerador}/{self.denominador} creado.")

    
    def __del__(self):
        print(f"Fracción {self.numerador}/{self.denominador} ha sido eliminada de la memoria.")

    
    def toString(self):
        return f"{self.numerador}/{self.denominador}"
   
    def sumar(self, otra):
        # Fórmula: (a/b) + (c/d) = (ad + bc) / bd
        nuevo_num = (self.numerador * otra.denominador) + (self.denominador * otra.numerador)
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def restar(self, otra):
        # Fórmula: (a/b) - (c/d) = (ad - bc) / bd
        nuevo_num = (self.numerador * otra.denominador) - (self.denominador * otra.numerador)
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def multiplicar(self, otra):
        # Fórmula: (a/b) * (c/d) = (ac) / (bd)
        nuevo_num = self.numerador * otra.numerador
        nuevo_den = self.denominador * otra.denominador
        return Fraccion(nuevo_num, nuevo_den)

    def dividir(self, otra):
        # Fórmula: (a/b) / (c/d) = (ad) / (bc)
        if otra.numerador == 0:
            print("No se puede dividir por una fracción con numerador cero.")
        nuevo_num = self.numerador * otra.denominador
        nuevo_den = self.denominador * otra.numerador
        return Fraccion(nuevo_num, nuevo_den)



f1 = Fraccion(1, 2)  # 1/2
f2 = Fraccion(3, 4)  # 3/4

resultado_suma = f1.sumar(f2)
print(f"Suma: {f1.toString()} + {f2.toString()} = {resultado_suma.toString()}")

res_resta = f1.restar(f2)
print(f"RESTA: {f1.toString()} - {f2.toString()} = {res_resta.toString()}")

resultado_mult = f1.multiplicar(f2)
print(f"Multiplicación: {f1.toString()} * {f2.toString()} = {resultado_mult.toString()}")

res_div = f1.dividir(f2)
print(f"DIVISIÓN: {f1.toString()} / {f2.toString()} = {res_div.toString()}")