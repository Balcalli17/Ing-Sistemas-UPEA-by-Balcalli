import random

class MetodoPago:
    def procesar_pago(self, monto):
        pass  # método base vacío

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        cvv = random.randint(1000, 9999)
        print(f"[TARJETA DE CRÉDITO]")
        print(f"  Verificando CVV: {cvv}")
        print(f"  Pago de Bs. {monto:.2f} procesado correctamente.")

class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        token = random.randint(100000, 999999)
        print(f"[PAYPAL]")
        print(f"  Token de seguridad generado: {token}")
        print(f"  Pago de Bs. {monto:.2f} procesado correctamente.")

class Efectivo(MetodoPago):
    def procesar_pago(self, monto):
        codigo = f"REF-{random.randint(10000, 99999)}"
        print(f"[EFECTIVO]")
        print(f"  Código de referencia para ventanilla: {codigo}")
        print(f"  Acérquese a pagar Bs. {monto:.2f} con este código.")

def ejecutar_transaccion(objeto_pago_elegido, monto):
    # Polimorfismo: no sabe qué tipo de pago es
    objeto_pago_elegido.procesar_pago(monto)

# ── Prueba de sistema ──
TASA_MUNICIPAL = 200

metodos = [TarjetaCredito(), PayPal(), Efectivo()]

print("=== COBRO DE TASA MUNICIPAL ===")
for metodo in metodos:
    print()
    ejecutar_transaccion(metodo, TASA_MUNICIPAL)
