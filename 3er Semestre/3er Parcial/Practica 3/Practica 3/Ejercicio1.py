import tkinter as tk
class Diseño:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.geometry("400x200")
        self.ventana.title("Primer grafico")
        self.ventana.configure(bg="#194bd5")
        self.ventana.columnconfigure(0,weight=1)
        self.componentes()

    def componentes(self):
        self.titulo=tk.Label(self.ventana,text="BIENVENIDO AL SISTEMA",
                             font=("Elephant",13,"bold"),bg="#194bd5")
        self.titulo.grid(row=0,columnspan=2,pady=10)

        #Boton
        self.boton=tk.Button(self.ventana,text="Ejecutar Accion",
                             command=self.ejecutado,
                             fg="#FFFFFF",
                             bg="#0f1233",font=("Arial",15))
        self.boton.grid(row=1,columnspan=2,pady=10)

        #resultado
        self.res=tk.Label(self.ventana,text="",
                          font=("Elephant",13,"bold"),
                          bg="#194bd5")
        self.res.grid(row=0,columnspan=2,pady=10)

    def ejecutado(self):
        self.titulo.grid_remove()
        self.res.config(text="BOTON PRECIONADO CON EXITO")

ventana=tk.Tk()
objeto=Diseño(ventana)
ventana.mainloop()
