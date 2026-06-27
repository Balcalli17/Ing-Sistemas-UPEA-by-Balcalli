import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora Básica")
        self.ventana.geometry("320x420")
        
        self.pantalla_var = tk.StringVar()
        
        self.construir_interfaz()
        
    def construir_interfaz(self):
        pantalla = tk.Entry(
            self.ventana, 
            textvariable=self.pantalla_var, 
            font=("Arial", 22), 
            bg="white", 
            bd=5, 
            relief="sunken", 
            justify="right"
        )
        pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=15, ipady=10, sticky="nsew")
        
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2)
        ]
        
        for (texto, fila, columna) in botones:
            tk.Button(
                self.ventana, text=texto, font=("Arial", 16),
                command=lambda t=texto: self.ingresar_caracter(t)
            ).grid(row=fila, column=columna, sticky="nsew", padx=3, pady=3)
        
        tk.Button(
            self.ventana, text='=', font=("Arial", 16), bg="lightgreen",
            command=self.calcular_resultado
        ).grid(row=4, column=3, sticky="nsew", padx=3, pady=3)
        
        tk.Button(
            self.ventana, text='C', font=("Arial", 16),
            command=self.limpiar_pantalla
        ).grid(row=5, column=2, sticky="nsew", padx=3, pady=3)
        
        tk.Button(
            self.ventana, text='OFF', font=("Arial", 16), bg="red", fg="white",
            command=self.ventana.destroy
        ).grid(row=5, column=3, sticky="nsew", padx=3, pady=3)
        
        for i in range(4):
            self.ventana.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.ventana.grid_rowconfigure(i, weight=1)

    def ingresar_caracter(self, caracter):
        estado_actual = self.pantalla_var.get()
        nuevo_estado = estado_actual + caracter
        self.pantalla_var.set(nuevo_estado)

    def limpiar_pantalla(self):
        self.pantalla_var.set("")

    def calcular_resultado(self):
        try:
            operacion = self.pantalla_var.get()
            resultado = str(eval(operacion))
            self.pantalla_var.set(resultado)
        except Exception:
            self.pantalla_var.set("Error")

def main():
    raiz = tk.Tk()
    aplicacion = Calculadora(raiz)
    raiz.mainloop()
main()