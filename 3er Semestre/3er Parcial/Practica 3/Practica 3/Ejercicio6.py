import tkinter as tk
from tkinter import messagebox
class Matriz:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Matriz")
        self.componentes()
    
    def componentes(self):
        self.titulo=tk.Label(self.ventana,text="MATRIZ")
        self.titulo.grid(row=0,columnspan=4,pady=10)

        self.enunciado=tk.Label(self.ventana,text="Dimension de matriz")
        self.enunciado.grid(row=1,column=0,padx=3,pady=8)

        self.n=tk.Entry(self.ventana,justify="center",width=10)
        self.n.grid(row=1,column=1,padx=3,pady=8)

        self.boton1=tk.Button(self.ventana,text="Generar",width=11,justify="center",command=self.generar)
        self.boton1.grid(row=1,column=2,padx=3,pady=8)

        self.boton2=tk.Button(self.ventana,text="Limpiar",justify="center",width=11,command=self.limpiar)
        self.boton2.grid(row=1,column=3,padx=3,pady=8)

        self.espacio=tk.Frame(self.ventana)
        self.espacio.grid(row=2,columnspan=4,pady=10)


    
    def crear(self):
        n=int(self.n.get())
        self.m=[0]*n
        for i in range(n):
            self.m[i]=[0]*n
    
    def generar(self):
        try:
            self.limpiar()
            n=int(self.n.get())
            for i in range(n):
                for j in range(n):
                    if i==j or i+j==n-1:
                        self.boton=tk.Button(self.espacio,text="1",justify="center",width=3,height=1)
                    else:
                        self.boton=tk.Button(self.espacio,text="0",justify="center",width=3,height=1)
                    self.boton.grid(row=i,column=j,sticky="news",padx=2,pady=1)

        except ValueError:
            messagebox.showerror("ERROR","El numero no es entero")

    def limpiar(self):
        for elemento in self.espacio.winfo_children():
            elemento.destroy()
ventana=tk.Tk()
objeto=Matriz(ventana)
ventana.mainloop()