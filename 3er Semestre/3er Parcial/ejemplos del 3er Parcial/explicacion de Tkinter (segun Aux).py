#Fundamentos de Tkinter 
#(input/Entry, print/Label, etc) => son eventos
import tkinter as tkinter
#fundamentos clave, o basicas para saber/crear
ventana = tkinter.Tk()
ventana.title("Ventana")
ventana.geometry("300x150")
ventana.configure(bg="blue") # configuracion, para dar estilo

#widgets basicos serian input, o print, que serian Entry y Label

#la mejor forma de crear nuestro widgets
lb_nombre = tkinter.Label(ventana,
                        text= "Hola mundo",
                        background="navy",
                        foreground="green",
                        font=("Arial", 15)).pack(pady=20, padx= 15)

en_nombre = tkinter.Entry(ventana,
                        selectbackground="green",
                        font=("Arial", 14)).pack()

#el "command" = evento, porque cuando hagas click, ejecuta algo 
def saludar():
    print("Hola")

btn_saludar = tkinter.Button(ventana,
                            text="Saludar",
                            command=saludar).pack()

ventana.mainloop()

