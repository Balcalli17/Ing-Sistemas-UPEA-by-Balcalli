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
            print(f"Retiro de Bs. {cantidad:.2f} realizado.")
        else:
            print(f"Saldo insuficiente. Saldo actual: Bs. {self.monto:.2f}")
        return self

    def __str__(self):
        return f"[{self.nro_de_cuenta}, {self.titular}, {self.monto:.2f}]"

# ── Programa principal ──
nro    = input("N° de cuenta : ")
titul  = input("Titular      : ")
monto  = float(input("Monto inicial: "))

cuenta = CuentaBancaria(nro, titul, monto)
print(f"\nCuenta creada: {cuenta}")

dep = float(input("\nMonto a depositar: "))
cuenta + dep
print(f"Tras depósito  : {cuenta}")

ret = float(input("Monto a retirar : "))
cuenta - ret
print(f"Tras retiro    : {cuenta}")
