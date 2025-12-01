# EJERCICIO Leer dos números de dos dígitos y determinar si tienen dígitos comunes

num1 = int(input("ingrese el 1er numero: "))
num2 = int(input("ingrese el 2do numero: "))

if 10 <= num1 <= 99 and 10 <= num2 <= 99:
    dig1_1 = num1 // 10
    dig1_2 = num1 % 10
    dig2_1 = num2 // 10
    dig2_2 = num2 % 10
    
    if (dig1_1 == dig2_1 or dig1_1 == dig2_2 or dig1_2 == dig2_1 or dig1_2 == dig2_2):
        print("los numeros tienen al menos un digito en comun.")
    else:
        print("los numeros NO tienen digitos en comun.")
else:
    print("solamente esta permitido numeros de dos digitos (10 al 99), ingrese nuevamente.")