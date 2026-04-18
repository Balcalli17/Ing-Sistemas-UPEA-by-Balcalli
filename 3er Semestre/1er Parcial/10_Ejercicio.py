class Producto:
    def _init_(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.stock = int(stock)

    @classmethod
    def desde_lista(cls, datos_lista):
        """Constructor alternativo que procesa una lista de datos"""
        # Desempaquetamos la lista directamente en el constructor
        return cls(datos_lista[0], datos_lista[1], datos_lista[2], datos_lista[3])

    def aplicar_descuento(self, porcentaje):
        """Calcula y resta el descuento al precio actual"""
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento
        print(f"--- Descuento aplicado al producto {self.nombre} ---")
        print(f"Nuevo precio: {self.precio} Bs.")

    def vender_unidades(self, cantidad):
        """Reduce el stock validando que haya suficiente"""
        if cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Venta exitosa: Se vendieron {cantidad} unidades de {self.nombre}.")
        else:
            print(f"Error: No hay suficiente stock de {self.nombre}. Stock disponible: {self.stock}")

    def reponer_unidades(self, cantidad):
        """Aumenta el stock del producto"""
        self.stock += cantidad
        print(f"Reposición: Se sumaron {cantidad} unidades a {self.nombre}.")

    def mostrar_informacion(self):
        """Muestra el estado actual del objeto"""
        print(f"\nID: {self.codigo} | Producto: {self.nombre}")
        print(f"Precio: {self.precio} Bs. | Stock: {self.stock} unidades")
        print("-" * 40)