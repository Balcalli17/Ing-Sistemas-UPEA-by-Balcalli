# EJERCICIO 10
import tkinter as tk
class Calculadora:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora Basica")
        self.componentes()

    def componentes(self):
        self.titulo=tk.Label(self.ventana,text="CALCULA BASICA",font=("Arial",11))
        self.titulo.grid(row=0,columnspan=2,pady=5)

        self.x=tk.Entry(self.ventana,width=20,state="normal",font=("Arial",11),justify="center")
        self.x.grid(row=1,column=0,pady=5,padx=5)
        self.x.insert(0,"numero X")
        self.x.config(state="disabled")

        self.y=tk.Entry(self.ventana,width=20,state="normal",font=("Arial",11),justify="center")
        self.y.grid(row=2,column=0,pady=5,padx=5)
        self.y.insert(0,"numero Y")
        self.y.config(state="disabled")        

        self.n1=tk.Entry(self.ventana,width=25,justify="center")
        self.n1.grid(row=1,column=1,padx=5)

        self.n2=tk.Entry(self.ventana,width=25,justify="center")
        self.n2.grid(row=2,column=1,padx=5)

        self.boton_suma=tk.Button(self.ventana,text="+",justify="center",font=("Arial",11),width=17,command=self.suma)
        self.boton_suma.grid(row=3,column=0,pady=2,padx=2)

        self.boton_resta=tk.Button(self.ventana,text="-",justify="center",font=("Arial",11),width=17,command=self.resta)
        self.boton_resta.grid(row=3,column=1,pady=2,padx=2)

        self.boton_multi=tk.Button(self.ventana,text="x",justify="center",font=("Arial",11),width=17,command=self.multi)
        self.boton_multi.grid(row=4,column=0,pady=2,padx=2)

        self.boton_div=tk.Button(self.ventana,text="/",justify="center",font=("Arial",11),width=17,command=self.division)
        self.boton_div.grid(row=4,column=1,pady=2,padx=2)

        self.boton_porcen=tk.Button(self.ventana,text="%",justify="center",font=("Arial",11),width=17,command=self.resto)
        self.boton_porcen.grid(row=5,column=0,pady=2,padx=2)

        self.boton_diventero=tk.Button(self.ventana,text="//",justify="center",font=("Arial",11),width=17,command=self.division_entera)
        self.boton_diventero.grid(row=5,column=1,pady=2,padx=2)

        self.boton_primosX=tk.Button(self.ventana,text="cPrimos(X)",justify="center",font=("Arial",11),width=17,command=self.primoX)
        self.boton_primosX.grid(row=6,column=0,pady=2,padx=2)

        self.boton_primosY=tk.Button(self.ventana,text="cPrimos(Y)",justify="center",font=("Arial",11),width=17,command=self.primoY)
        self.boton_primosY.grid(row=6,column=1,pady=2,padx=2)

        self.boton_ce=tk.Button(self.ventana,text="CE",justify="center",font=("Arial",11),width=36,command=self.limpiar)
        self.boton_ce.grid(row=7,columnspan=2,pady=2,padx=2)

        self.res=tk.Entry(self.ventana,justify="center",font=("Arial",11),width=40,state="disabled",disabledbackground="#fbff00")
        self.res.grid(row=8,columnspan=2,pady=2,padx=2)

    def suma(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            self.res.insert(0,f"{n1+n2}")

            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")

    def resta(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            self.res.insert(0,f"{n1-n2}")

            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")
    
    def multi(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            self.res.insert(0,f"{n1*n2}")

            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")

    def division(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            self.res.insert(0,f"{n1/n2}")

            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")

    def resto(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            self.res.insert(0,f"{n1%n2}")

            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")

    def division_entera(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n1=int(self.n1.get())
            n2=int(self.n2.get())
            self.res.insert(0,f"{n1//n2}")

            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")
    def es_primo(self,num):
        c=0
        for i in range(1,num+1):
            if num%i==0:
                c=c+1
        if c==2:
            return True
        else:
            return False
            
    def primoX(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n1=int(self.n1.get())
            cantidad=0
            n=n1
            while n>0:
                digito=n%10
                if self.es_primo(digito)==True:
                    cantidad=cantidad+1
                n=n//10
            self.res.insert(0,f"Hay {cantidad} numero primos")
            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")

    def primoY(self):
        self.res.config(state="normal")
        try:
            self.res.delete(0,tk.END)
            n2=int(self.n2.get())
            cantidad=0
            n=n2
            while n>0:
                digito=n%10
                if self.es_primo(digito)==True:
                    cantidad=cantidad+1
                n=n//10
            self.res.insert(0,f"Hay {cantidad} numero primos")
            self.res.config(state="disabled")
            
        except ValueError:
            self.res.insert("Error no es entero")
            self.res.config(state="disabled")
    
    def limpiar(self):
        self.n1.delete(0,tk.END)
        self.n2.delete(0,tk.END)
        self.res.config(state="normal")
        self.res.delete(0,tk.END)
        self.res.config(state="disabled")
        
ventana=tk.Tk()
calcu=Calculadora(ventana)
ventana.mainloop()