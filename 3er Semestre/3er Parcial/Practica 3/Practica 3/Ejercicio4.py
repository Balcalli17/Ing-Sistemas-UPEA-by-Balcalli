import tkinter as tk
class Conversor:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.geometry("320x250")
        self.ventana.title("CONVERSOR DE MONEDA")
        self.ventana.config(bg="#131949")
        self.componentes()
    
    def componentes(self):
        self.enunciado=tk.Label(self.ventana,text="Ingrese el monto en Bolivianos(Bs)",
                                font=("Arial",13,"bold"),fg="white",bg="#131949")
        self.enunciado.pack(pady=12)

        self.n=tk.Entry(self.ventana,width=18,font=("Arial",13),justify="center")
        self.n.pack(pady=10)

        self.boton=tk.Button(self.ventana,text="Convertir a Dólares",font=("Arial",15,"bold"),
                                fg="white",bg="#1489ff",command=self.convertir)
        self.boton.pack(pady=10)

        self.res=tk.Label(self.ventana,text="Resultado: ",font=("Arial",13,"bold"),bg="#131949",fg="#29d4ff")
        self.res.pack(pady=10)
    
    def convertir(self):
        try:
            n=float(self.n.get())
            resultado=n/6.96
            self.res.config(text=f"Resultado: $ {resultado:.2f}")
        except ValueError:
            self.res.config(text="No es entero")

ventana=tk.Tk()
objeto=Conversor(ventana)
ventana.mainloop()