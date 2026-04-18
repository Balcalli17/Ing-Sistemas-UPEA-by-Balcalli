class Lista_de_numeros:
    def __init__(self, lista):
        # El doble guion bajo hace que el atributo sea privado en Python
        self.__numeros = lista 

    def suma_total(self):
        return sum(self.__numeros)

    def promedio(self):
        if len(self.__numeros) == 0:
            return 0.0
        return sum(self.__numeros) / len(self.__numeros)

    def el_maximo(self):
        if not self.__numeros: 
            return None
        return max(self.__numeros)

    def el_minimo(self):
        if not self.__numeros: 
            return None
        return min(self.__numeros)

    def mostrar_lista(self):
        # Muestra todos los resultados según lo solicitado [cite: 207]
        print(f"Lista de números: {self.__numeros}")
        print(f"Suma Total: {self.suma_total()}")
        print(f"Promedio: {self.promedio():.2f}")
        print(f"Valor Máximo: {self.el_maximo()}")
        print(f"Valor Mínimo: {self.el_minimo()}")
        print("-" * 30)

# --- PROGRAMA PRINCIPAL ---
# Instanciar dos objetos con las listas requeridas [cite: 211]
lista1 = Lista_de_numeros([10, 5, 7, 12, 8, 20])
lista2 = Lista_de_numeros([5, 1, 3, 9, 10])

# Llamar al método para mostrar cálculos [cite: 212]
print("Resultados Instancia 1:")
lista1.mostrar_lista()

print("Resultados Instancia 2:")
lista2.mostrar_lista()