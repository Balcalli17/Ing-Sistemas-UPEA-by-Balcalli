import tkinter as tk

class AnalizadorGenerico:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("550x420")
        self.ventana.title("Analizador Genérico y RTTI - UPEA")
        self.ventana.config(bg="#1c1d31")
        self.componentes()
    
    def componentes(self):
        self.titulo = tk.Label(
            self.ventana, 
            text="LABORATORIO: RTTI Y PROGRAMACIÓN GENÉRICA",
            font=("Arial", 14, "bold"), 
            fg="#f1a7ff", 
            bg="#1c1d31"
        )
        self.titulo.pack(pady=20)

        self.enunciado = tk.Label(
            self.ventana, 
            text="Ingrese un dato cualquiera (Texto, Entero o Decimal):",
            font=("Arial", 12), 
            fg="#e0e0e0", 
            bg="#1c1d31"
        )
        self.enunciado.pack(pady=10)

        self.entrada = tk.Entry(
            self.ventana, 
            width=30, 
            font=("Arial", 14), 
            justify="center", 
            bg="#2c2d44", 
            fg="white", 
            insertbackground="white"
        )
        self.entrada.pack(pady=10)

        self.boton = tk.Button(
            self.ventana, 
            text="🔍 Identificar Tipo de Dato", 
            font=("Arial", 12, "bold"),
            fg="black", 
            bg="#70a6ff", 
            command=self.identificar_tipo,
            padx=10, 
            pady=5
        )
        self.boton.pack(pady=20)

        self.lbl_runtime = tk.Label(
            self.ventana, 
            text="Tipo de dato en Runtime: ---",
            font=("Arial", 12, "italic"), 
            fg="#b0b0c5", 
            bg="#1c1d31"
        )
        self.lbl_runtime.pack(pady=5)

        self.lbl_resultado = tk.Label(
            self.ventana, 
            text="Esperando entrada...", 
            font=("Arial", 13, "bold"), 
            bg="#25263f", 
            fg="#a3e2a5",
            width=45,
            height=2
        )
        self.lbl_resultado.pack(pady=20)
    
    def identificar_tipo(self):
        valor_original = self.entrada.get()
        try:
            valor_convertido = int(valor_original)
            tipo_detectado = "INT"
        except ValueError:
            try:
                valor_convertido = float(valor_original)
                tipo_detectado = "FLOAT"
            except ValueError:
                valor_convertido = valor_original
                tipo_detectado = "STR"
        
        if tipo_detectado == "INT":
            cuadrado = valor_convertido ** 2
            self.lbl_runtime.config(text=f"Tipo de dato en Runtime: {tipo_detectado}")
            self.lbl_resultado.config(text=f"Es un ENTERO. Su cuadrado es: {cuadrado}")
            
        elif tipo_detectado == "FLOAT":
            mitad = valor_convertido / 2
            self.lbl_runtime.config(text=f"Tipo de dato en Runtime: {tipo_detectado}")
            self.lbl_resultado.config(text=f"Es un DECIMAL. Su mitad es: {mitad:.2f}")
        else:
            longitud = len(valor_convertido)
            self.lbl_runtime.config(text=f"Tipo de dato en Runtime: {tipo_detectado}")
            self.lbl_resultado.config(text=f"Es una CADENA. Su longitud es: {longitud} caracteres")

ventana = tk.Tk()
app = AnalizadorGenerico(ventana)
ventana.mainloop()