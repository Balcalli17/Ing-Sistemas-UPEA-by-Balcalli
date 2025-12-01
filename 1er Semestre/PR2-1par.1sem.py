#2. Escribe un programa que cuente la cantidad de dígitos de un número entero dado.

#------------------------------------------------------------------------------------------------------------
#1ro. solicitamos un numero por pantalla.
n=int(input("ingrese un numero: "))
cont=0 #este es un contador de digitos.

#por si el numero solicitado es negativo.
if n<0:
    n=n*-1
#por si el numero solicitado es cero.
if n == 0:
    cont = 1
else: #de aqui empieza a girar el bucle.
    while n>0:
        n = n // 10
        cont=cont+1

#imprimimos por pantalla cuandos digitos tiene el numero.
print(f"el numero solicitado tiene {cont} digitos.")