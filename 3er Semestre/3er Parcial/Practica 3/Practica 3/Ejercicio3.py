import tkinter as tk

class Primo:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("300x250")
        self.ventana.title("Primo?")
        self.componentes()
    
    def componentes(self):
        self.titulo = tk.Label(self.ventana, text="Es primo?",
                               bg="#94e881", font=("Arial", 11))
        self.titulo.grid(row=0, columnspan=2)

        self.enunciado = tk.Label(self.ventana, text="Numero entero",
                                  font=("Arial", 11), fg="#0015fc")
        self.enunciado.grid(row=1, column=0, pady=10, padx=10)

        self.entrada = tk.Entry(self.ventana, width=15, justify="center", font=("Arial", 12))
        self.entrada.grid(row=1, column=1, padx=15)

        self.boton1 = tk.Button(self.ventana, text="Primo?", command=self.es_primo)
        self.boton1.grid(row=3, columnspan=2, pady=5)

        self.boton2 = tk.Button(self.ventana, text="Limpiar", command=self.limpiar)
        self.boton2.grid(row=4, columnspan=2, pady=5)

        self.cuadro = tk.Entry(self.ventana, width=15, font=("Arial", 12), state="disabled",
                               disabledbackground="#2bfbff", disabledforeground="black",justify="center")
        self.cuadro.grid(row=5, columnspan=2, pady=5)
    
    def es_primo(self):
        try:
            entrada = int(self.entrada.get())
            self.cuadro.config(state="normal")
            self.cuadro.delete(0, tk.END)
            c = 0
            for i in range(1, entrada + 1):
                if entrada % i == 0:
                    c = c + 1
            if c == 2:
                self.cuadro.insert(tk.END, f"{entrada} Es Primo")
            else:
                self.cuadro.insert(tk.END, f"{entrada} No es Primo")
                
            self.cuadro.config(state="disabled")
            
        except ValueError:
            self.cuadro.config(state="normal")
            self.cuadro.delete(0, tk.END)
            self.cuadro.insert(tk.END, "Error: pon un entero")
            self.cuadro.config(state="disabled")
        
    def limpiar(self):
        self.entrada.delete(0, tk.END)
        
        self.cuadro.config(state="normal")
        self.cuadro.delete(0, tk.END) 
        self.cuadro.config(state="disabled")
    
ventana = tk.Tk()
objeto = Primo(ventana)
ventana.mainloop()