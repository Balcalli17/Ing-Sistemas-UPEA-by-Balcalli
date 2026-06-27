import tkinter as tk
from tkinter import messagebox
class Suma_enteros:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.geometry("350x200")
        self.ventana.title("Suma de enteros")
        self.componentes()
    
    def componentes(self):
        self.enunciado1=tk.Label(self.ventana,text="Ingrese Numero 1:",font=("Arial",11))
        self.enunciado1.grid(row=0,column=0,pady=15,padx=15)

        self.n1=tk.Entry(self.ventana,width=20,font=("Arial",11),justify="center")
        self.n1.grid(row=0,column=1,padx=10,pady=5)

        self.enunciado2=tk.Label(self.ventana,text="Ingrese Numero 2:",font=("Arial",11))
        self.enunciado2.grid(row=1,column=0,padx=15,pady=15)

        self.n2=tk.Entry(self.ventana,width=20,font=("Arial",11),justify="center")
        self.n2.grid(row=1,column=1,padx=10,pady=5)

        # Boton 1
        self.boton1=tk.Button(self.ventana,text="Sumar",font=("Arial",11),width=10,command=self.sumar)
        self.boton1.grid(row=2,column=0)
        # Boton 2
        self.boton2=tk.Button(self.ventana,text="Limpiar",font=("Arial",11),width=10,command=self.limpiar)
        self.boton2.grid(row=2,column=1)

        # Resultado
        self.res=tk.Label(self.ventana,text="Resultado:",font=("Arial",11))
        self.res.grid(row=3,columnspan=2,pady=10)
    
    def sumar(self):
        try:
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            self.res.config(text=f"Resultado: {n1} + {n2} = {n1+n2}")

        except ValueError:
            messagebox.showerror("Error de datos", "Por favor, introduzca solo números enteros.")
    
    def limpiar(self):
        self.n1.delete(0,tk.END)
        self.n2.delete(0,tk.END)
        self.res.config(text="Resultado:")


ventana=tk.Tk()
objeto=Suma_enteros(ventana)
ventana.mainloop()