import tkinter as tk
class Monto:
    def __init__(self, saldo):
        self.__saldo=saldo
    
    def obtener(self):
        return self.__saldo
    
class Cuenta:
    def __init__(self, ventana, saldo):
        self.ventana=ventana
        self.ventana.geometry("300x60")
        self.mi_cuenta=Monto(saldo)
        self.ventana.columnconfigure(0,weight=1)
        self.mostrar()
    
    def mostrar(self):
        texto=self.mi_cuenta.obtener()
        self.monto=tk.Label(self.ventana, text=f"Saldo: {texto}")
        self.monto.grid(row=0,columnspan=2,pady=10)

ventana=tk.Tk()
objeto=Cuenta(ventana,1000)
ventana.mainloop()