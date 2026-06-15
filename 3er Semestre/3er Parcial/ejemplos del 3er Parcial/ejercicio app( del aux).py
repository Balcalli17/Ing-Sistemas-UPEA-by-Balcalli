#Ejercicio 12 de la practica:
import tkinter as tk
import random

class AdivinaNumero:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina, el adivinador")
        self.root.geometry("300x350")
        self.root.configure(bg= "blue")

        self.num_secreto = random.randint(1,10)
        # titulo
        tk.Label(root,
                text="ADIVINA",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="blue",
                ).pack(pady=10)
        
        #Entrada => Frame

        frame = tk.Frame(root, background="blue")
        frame.pack(pady=5)

        tk.Label(frame,
                text="Numero entre 1 y 10",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="blue",
                ).grid(row=0, column=0, padx=5)
        
        self.entrada = tk.Entry(frame,
                                justify="center",
                                font=("Arial",12))
        
        self.entrada.grid(row=0, column=1)

        # botones => frame

        btn_frame = tk.Frame(root, background="blue")
        btn_frame.pack(pady=10)

        self.btn_verificar = tk.Button(btn_frame,
                                    text="Verificar")
        self.btn_verificar.grid(row=0,column=1,padx=5)

        self.btn_limpiar = tk.Button(btn_frame,
                                    text="limpiar",
                                    background="green")
        self.btn_limpiar.grid(row=0,column=1,padx=5)

        tk.Label(root,
                text="RESULTADO",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="blue",
                ).pack(pady=10)
        
        self.resultado = tk.Label(root,
                                text="S/N",
                                font=("Arial",12),
                                ).pack(pady=10)
        
    def verificar(self):
        try:
            num = int(self.entrada.get())
            if num < 1 or num > 10:
                self.resultado.config(text="Solo entre 1 y 10")
                return
            self.intentos +=1

            if num == self.num_secreto:
                self.resultado.config(text="adivino, en ... intentos")
            elif num < self.num_secreto:
                self.resultado.config(text="el numero es mayor")
            else:
                self.resultado.config(text="el numero es menor")

if __name__ == "__main__":
    root = tk.Tk() #la instancia principal, o tambien le puedes llamar ventana

    app = AdivinaNumero(root)

    root.mainloop()