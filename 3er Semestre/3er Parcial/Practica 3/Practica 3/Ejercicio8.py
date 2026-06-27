import tkinter as tk
from tkinter import messagebox
class matriz_cuadrada:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Matriz")
        self.componentes()
    
    def componentes(self):
        self.titulo=tk.Label(self.ventana,text="UN CUADRADO",fg="red")
        self.titulo.grid(row=0,columnspan=3,pady=15)

        self.enunciado=tk.Label(self.ventana,text="Dimension",fg="blue")
        self.enunciado.grid(row=1,column=0,padx=3,pady=10)

        self.n=tk.Entry(self.ventana,width=15,justify="center")
        self.n.grid(row=1,column=1,padx=3,pady=10)

        self.boton=tk.Button(self.ventana,text="Generar",width=9,justify="center",command=self.generar)
        self.boton.grid(row=1,column=2,padx=3,pady=10)

        self.espacio=tk.Frame(self.ventana)
        self.espacio.grid(row=2,columnspan=3,pady=10)
    
    
    def crear_matriz(self):
        n=int(self.n.get())
        self.matriz=[0]*n
        for i in range(n):
            self.matriz[i]=[0]*n
    
    def generar(self):
        try:
            self.limpiar()
            n=int(self.n.get())
            for i in range(n):
                for j in range(n):
                    if i==n-1 or j==n-1 or i>=j and j==0 or i==0:
                        boton=tk.Button(self.espacio, text="▓",width=3,height=1)
                        boton.grid(row=i,column=j,padx=2,pady=1,sticky="news")
                    else:
                        boton=tk.Button(self.espacio,width=3,height=1)
                        boton.grid(row=i,column=j,padx=2,pady=1,sticky="news")

        except ValueError:
            messagebox.showerror("Error","No es entero")
    def limpiar(self):
        for elemento in self.espacio.winfo_children():
            elemento.destroy()
                
                


ventana=tk.Tk()
objeto=matriz_cuadrada(ventana)
ventana.mainloop()