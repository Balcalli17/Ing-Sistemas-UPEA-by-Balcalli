class NumeroEspecial:
    def __init__(self, x):
        self.x = x # Inicialización de la variable x [cite: 119]

    def es_primo(self):
        if self.x < 2:
            return False
        for i in range(2, int(self.x**0.5) + 1):
            if self.x % i == 0:
                return False
        return True

    def es_perfecto(self):
        if self.x < 2:
            return False
        # Suma de los divisores propios del número
        suma_divisores = sum(i for i in range(1, self.x) if self.x % i == 0)
        return suma_divisores == self.x

    def cantidad_digitos(self):
        return len(str(self.x))

    def rotar_izquierda(self, k):
        s = str(self.x)
        if len(s) == 0: return self.x
        k = k % len(s) # Maneja casos donde k es mayor que la cantidad de dígitos
        rotado = s[k:] + s[:k]
        return int(rotado)

# --- PROGRAMA PRINCIPAL ---
print("--- LOTE DE NÚMEROS ---")
x = int(input("Ingrese valor para x (>= 8100): "))
y = int(input("Ingrese valor para y (> x): "))

# Validación de entrada [cite: 125]
if x >= 8100 and y > x:
    k = 3 # Constante de rotación para números perfectos según el ejemplo [cite: 131]
    print(f"\nSALIDA:\nk={k}")
    
    for num in range(x, y + 1):
        obj_num = NumeroEspecial(num)

        # Verificar y mostrar si es primo [cite: 126, 132]
        if obj_num.es_primo():
            rotado_1 = obj_num.rotar_izquierda(1)
            print(f"PRIMO {num}, ROTA IZQ. 1 VEZ: {rotado_1}")

        # Verificar y mostrar si es perfecto [cite: 126, 139]
        if obj_num.es_perfecto():
            rotado_k = obj_num.rotar_izquierda(k)
            print(f"PERFECTO {num}, ROTA IZQ. {k} VECES: {rotado_k}")
else:
    print("Valores fuera de rango. Fin del programa.")