#4. Leer un número entero de tres dígitos y hallar la suma total de sus dígitos. (Aplicar estructura secuencial).
#-------------------------------------------------------------------------------------------------------------
n=int(input("ingrese un numero de tres digitos: "))
suma=0
if n>=100 and n<=999:
    n100= n // 100
    n10= (n // 10) % 10
    n1= n % 10
    suma = n100 + n10 + n1
else:
    print("ingrese un numero de 3 digitos (del 100 al 999).")

print(f"la suma de los digitos del numero ingresado es: {suma}")