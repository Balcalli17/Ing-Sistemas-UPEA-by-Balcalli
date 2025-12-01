num1 = int(input("ingrese primer numero: "))
num2 = int(input("ingrese segundo numero: "))

operacion = input("ingrese la operacion (S: suma, R: resta, M: multiplicacion, D: division): ")
if operacion == 'S':
    resultado = num1 + num2
    print(f"el resultado de la suma es: {resultado}")
elif operacion == 'R':
    resultado = num1 - num2
    print(f"el resultado de la resta es: {resultado}")
elif operacion == 'M':
    resultado = num1 * num2
    print(f"el resultado de la multiplicacion es: {resultado}")
elif operacion == 'D':
    if num2 == 0:
        print("no se puede dividir entre cero")
    else:
        resultado = num1/num2
        print(f"el resultado de la division es: {resultado}")
else:
    print("opcion no valida")