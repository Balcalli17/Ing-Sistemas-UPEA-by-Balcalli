import tkinter as tk
from tkinter import messagebox
import random

class Adivina:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Adivina, Adivina")
        self.ventana.config(bg="blue")
        self.num_aleatorio = random.randint(1, 10)
        self.intentos = 0 
        
        self.componentes()
    
    def componentes(self):
        self.titulo=tk.Label(self.ventana,text="ADIVINA",fg="yellow",bg="blue",font=("Arial",11,))
        self.titulo.grid(row=0,columnspan=2,pady=10)

        self.enunciado=tk.Label(self.ventana,text="Numero entre 1 y 10",bg="blue",font=("Arial",11),fg="yellow")
        self.enunciado.grid(row=1,column=0,padx=10,pady=10)

        self.n=tk.Entry(self.ventana,width=10,justify="center",font=("Arial",11))
        self.n.grid(row=1,column=1,padx=10,pady=10)

        self.boton1=tk.Button(self.ventana,text="Verificar",bg="#7ee275",justify="center",font=("Arial",11),command=self.adivina_num)
        self.boton1.grid(row=2,column=0,padx=10,pady=10)

        self.boton2=tk.Button(self.ventana,text="Limpiar",bg="#7ee275",justify="center",font=("Arial",11),command=self.limpiar_juego)
        self.boton2.grid(row=2,column=1,padx=10,pady=10)

        self.res=tk.Label(self.ventana,text="RESULTADO:",font=("Arial",11),fg="yellow",bg="blue")
        self.res.grid(row=3,columnspan=2,padx=10,pady=10)

        self.mostrar=tk.Label(self.ventana,text="",font=("Arial",11),justify="center",bg="blue",fg="white")
        self.mostrar.grid(row=4,columnspan=2,padx=10,pady=10)
    
    def adivina_num(self):
        try:
            texto_ingresado = self.n.get()
            n = int(texto_ingresado)
            
            if n < 1 or n > 10:
                messagebox.showerror("ERROR!", "EL NUMERO DEBE ESTAR ENTRE 1 Y 10")
                return

            self.intentos += 1
            
            if n == self.num_aleatorio:
                self.mostrar.config(text=f"ADIVINÓ, en {self.intentos} intentos")
            elif n > self.num_aleatorio:
                self.mostrar.config(text=f"{n} es MAYOR al número a adivinar")
            else:
                self.mostrar.config(text=f"{n} es MENOR al número a adivinar")
                
        except ValueError:
            messagebox.showerror("ERROR!", "EL VALOR DEBE SER UN NÚMERO ENTERO VÁLIDO")

    def limpiar_juego(self):
        self.num_aleatorio = random.randint(1, 10)
        self.intentos = 0
        self.n.delete(0, tk.END)
        self.mostrar.config(text="")

ventana=tk.Tk()
objeto=Adivina(ventana)
ventana.mainloop()