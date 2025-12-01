#1.Leer un número entero y determinar si es un número terminado en 4
#--------------------------------------------------------------------------------------------------------------
#1ro. pedimos un numero por pantalla
n = int(input("ingrese un numero: "))

#2do. al numero solicitado lo dividimos entre 10 para obtener el residuo.
ult_num= n % 10

#3ro. a nuestra ultima variable obtenida, lo preguntamos si es igual a 4.
if ult_num == 4:
    print("el numero solicitado termina en 4.")
else:
    print("el numero solicitado no termina en 4.")