import tkinter as tk
from tkinter import messagebox
class Matriz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Matriz")
        self.componentes()
    
    def componentes(self):
        self.titulo=tk.Label(self.ventana,text="MATRIZ")
        self.titulo.grid(row=0,columnspan=3,pady=8)

        self.enunciado1=tk.Label(self.ventana,text="Filas:")
        self.enunciado1.grid(row=1,column=0,pady=10,padx=10)

        self.enunciado2=tk.Label(self.ventana,text="Columnas:")
        self.enunciado2.grid(row=2,column=0,pady=10,padx=5)

        self.n1=tk.Entry(self.ventana,width=15,justify="center")
        self.n1.grid(row=1,column=1,pady=10)

        self.n2=tk.Entry(self.ventana,width=15,justify="center")
        self.n2.grid(row=2,column=1,pady=10)

        self.boton1=tk.Button(self.ventana,text="Generar",justify="center",command=self.generar)
        self.boton1.grid(row=1,column=2,pady=10,padx=5)

        self.boton1=tk.Button(self.ventana,text="Limpiar",justify="center",command=self.limpiar)
        self.boton1.grid(row=2,column=2,pady=10,padx=5)

        self.espacio=tk.Frame(self.ventana)
        self.espacio.grid(row=3,columnspan=3)

    def crear(self):
        n1=int(self.n1.get())
        n2=int(self.n2.get())
        self.m=[0]*n1
        for i in range(n1):
            self.m[i]=[0]*n2
    
    def generar(self):
        self.limpiar()
        try:
            c=1
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            for i in range(n1):
                for j in range(n2):
                    if i % 2 == 0:
                        self.boton=tk.Button(self.espacio,text=c,width=3,height=1)
                        self.boton.grid(row=i,column=j,padx=1,pady=3)
                    else:
                        pos = (n2 - 1) - j
                        self.boton=tk.Button(self.espacio,text=c,width=3,height=1)
                        self.boton.grid(row=i,column=pos,padx=1,pady=3)
                    c=c+1
                print("")                    
        except ValueError:
            messagebox.showerror("Error","NO ES ENTERO")
    def limpiar(self):
        for elemento in self.espacio.winfo_children():
            elemento.destroy()

ventana=tk.Tk()
objeto=Matriz(ventana)
ventana.mainloop()