#3. Escribe un programa para determinar si el año ingresado es bisiesto o no.
#--------------------------------------------------------------------------------------------------------------
#1ro solicitamos un numero por pantalla.
año=int(input("ingrese un año por pantalla: "))
#2do si año es divisible por 4 y su residuo es 0, es bisiesto, sino no lo es.
if año % 4 == 0:
    print("es año bisiesto")
else:
    print("no es año bisiesto")