import tkinter as tk
class ConversorMoneda:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Conversor de Moneda")
        self.ventana.geometry("400x400")
        self.ventana.configure(bg="#45556C")

        self.etiqueta=tk.Label(ventana,
            text="Ingrese el monto en Bolivianos (Bs.): ",
            font=("Arial",15,"bold"),
            bg="#45556C",
            fg="#F8FAFC")
        self.etiqueta.pack(pady=15)

        self.caja_monto=tk.Entry(ventana,
            font=("Arial",15),
            justify="center")
        self.caja_monto.pack(pady=5)

        self.boton_convertir=tk.Button(ventana,
            text="Convertir a Dolares",
            command=self.procesar_conversion,
            font=("Arial",15,"bold"),
            bg="#21BCFF",
            fg="#F0FDF4")
        self.boton_convertir.pack(pady=10)

        self.etiqueta_resultado=tk.Label(ventana,
            text="Resultado:$ 0.00",
            font=("Arial",15,"bold"),
            bg="#45556C",
            fg="#F8FAFC")
        self.etiqueta_resultado.pack(pady=20)
    
    def procesar_conversion(self):
        bolivianos = float(self.caja_monto.get())
        dolares = bolivianos/6.96
        self.etiqueta_resultado.config(text=f"Resultado:$ {dolares:.2f}")

def main():
    raiz = tk.Tk()
    app = ConversorMoneda(raiz)
    raiz.mainloop()
main()