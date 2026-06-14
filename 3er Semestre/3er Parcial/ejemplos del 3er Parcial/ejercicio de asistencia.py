import tkinter as tk
from tkinter import messagebox

# ── Clase CuentaBancaria (Se mantiene intacta tu lógica original) ──
class CuentaBancaria:
    def __init__(self, nro_de_cuenta, titular, monto):
        self.nro_de_cuenta = nro_de_cuenta
        self.titular       = titular
        self.monto         = monto

    def __add__(self, cantidad):
        self.monto += cantidad
        return self

    def __sub__(self, cantidad):
        if self.monto >= cantidad:
            self.monto -= cantidad
            return True, f"¡Retiro de {cantidad:.1f} Bs. exitoso!"
        else:
            return False, f"Saldo insuficiente. Saldo actual: {self.monto:.1f} BS"

    def __str__(self):
        return f"Nro. Cuenta: {self.nro_de_cuenta} | Titular: {self.titular} | Saldo: {self.monto:.1f} BS"


# ── Interfaz Gráfica adaptada al diseño de las capturas ──
class AppBancaria:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión Bancaria - UPEA")
        self.root.geometry("480x420")
        
        # Paleta de colores basada en tus imágenes
        self.COLOR_FONDO = "#111E30"       # Azul oscuro de fondo
        self.COLOR_PANEL = "#16263B"       # Recuadro superior un poco más claro
        self.COLOR_TEXTO_VERDE = "#2ECC71"  # Verde brillante para los datos y éxito
        self.COLOR_BTN_DEPOSITAR = "#00875A" # Verde del botón depositar
        self.COLOR_BTN_RETIRAR = "#D32F2F"   # Rojo del botón retirar

        self.root.configure(bg=self.COLOR_FONDO)
        self.root.resizable(False, False)

        # Crear una cuenta por defecto como se ve en tu ejemplo para que inicie directo en esa pantalla
        self.cuenta = CuentaBancaria("103", "Juan Perez", 4300.0)

        # ── 1. PANEL SUPERIOR (Datos de la cuenta) ──
        self.frame_info = tk.Frame(root, bg=self.COLOR_PANEL, padx=10, pady=10)
        self.frame_info.pack(fill="x", padx=20, pady=25)

        self.lbl_info = tk.Label(
            self.frame_info, 
            text=str(self.cuenta), 
            font=("Arial", 11, "bold"), 
            fg=self.COLOR_TEXTO_VERDE, 
            bg=self.COLOR_PANEL
        )
        self.lbl_info.pack()

        # ── 2. ETIQUETA DE INSTRUCCIÓN ──
        lbl_instruccion = tk.Label(
            root, 
            text="Ingrese la cantidad en Bs.", 
            font=("Arial", 11), 
            fg="#5C6B73", 
            bg=self.COLOR_FONDO
        )
        lbl_instruccion.pack(pady=5)

        # ── 3. CAJA DE ENTRADA (Monto a operar) ──
        self.entry_monto = tk.Entry(
            root, 
            font=("Arial", 16), 
            justify="center", 
            width=22,
            bd=0,
            highlightthickness=0
        )
        self.entry_monto.pack(pady=10)
        self.entry_monto.insert(0, "500") # Valor inicial sugerido en tu ejemplo

        # ── 4. BOTÓN REALIZAR DEPÓSITO ──
        self.btn_deposito = tk.Button(
            root, 
            text="Realizar Depósito", 
            font=("Arial", 11, "bold"), 
            bg=self.COLOR_BTN_DEPOSITAR, 
            fg="white", 
            width=22, 
            height=1,
            bd=1,
            relief="raised",
            command=self.ejecutar_deposito
        )
        self.btn_deposito.pack(pady=8)

        # ── 5. BOTÓN REALIZAR RETIRO ──
        self.btn_retiro = tk.Button(
            root, 
            text="Realizar Retiro", 
            font=("Arial", 11, "bold"), 
            bg=self.COLOR_BTN_RETIRAR, 
            fg="white", 
            width=22, 
            height=1,
            bd=1,
            relief="raised",
            command=self.ejecutar_retiro
        )
        self.btn_retiro.pack(pady=8)

        # ── 6. ETIQUETA DE ESTADO / RESULTADO INFERIOR ──
        self.lbl_estado = tk.Label(
            root, 
            text="Operaciones listas.", 
            font=("Arial", 11, "italic"), 
            fg="#7F8C8D", 
            bg=self.COLOR_FONDO
        )
        self.lbl_estado.pack(pady=20)


    # ── Lógica de los botones vinculada a los operadores sobrecargados ──
    def ejecutar_deposito(self):
        try:
            cantidad = float(self.entry_monto.get())
            if cantidad <= 0:
                self.mostrar_mensaje(f"Monto inválido", es_error=True)
                return
            
            # Llama al operador __add__ de tu clase original
            self.cuenta + cantidad
            
            # Actualiza la vista
            self.lbl_info.config(text=str(self.cuenta))
            self.mostrar_mensaje(f"¡Depósito de {cantidad:.1f} Bs. exitoso!", es_error=False)
        except ValueError:
            self.mostrar_mensaje("Inserte un valor numérico", es_error=True)

    def ejecutar_retiro(self):
        try:
            cantidad = float(self.entry_monto.get())
            if cantidad <= 0:
                self.mostrar_mensaje(f"Monto inválido", es_error=True)
                return
            
            # Llama al operador __sub__ de tu clase original
            exito, mensaje = self.cuenta - cantidad
            
            # Actualiza la vista
            self.lbl_info.config(text=str(self.cuenta))
            self.mostrar_mensaje(mensaje, es_error=not exito)
        except ValueError:
            self.mostrar_mensaje("Inserte un valor numérico", es_error=True)

    def mostrar_mensaje(self, mensaje, es_error):
        # Cambia dinámicamente el color del texto inferior dependiendo del resultado
        if es_error:
            self.lbl_estado.config(text=mensaje, fg=self.COLOR_BTN_RETIRAR)
        else:
            self.lbl_estado.config(text=mensaje, fg=self.COLOR_TEXTO_VERDE)


# ── Ejecución de la aplicación ──
if __name__ == "__main__":
    ventana = tk.Tk()
    app = AppBancaria(ventana)
    ventana.mainloop()