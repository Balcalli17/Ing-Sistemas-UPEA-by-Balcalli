#FUNCIONES
def suma_dig(num): #creamos una funcion para el problema
    s = 0 #creamos una variable para almacenar la suma de digitos
    while(num > 0): #preguntamos: si "num" es mayor a cero, se ejecuta el procedimiento de abajo
        d = num % 10
        s = s + d
        num = num // 10 #una vez procesado, vuelve a preguntar, hasta que "num" no sea mayor a cero
    return s
#PRINCIPAL
while(True):
    n=int(input("ingresa el valor de n entero positivo por pantalla: "))
    if n > 0:
        break
    
sum = suma_dig(n)

print(f"la suma del numero {n} es {sum}.")