#leer dos numeros enteros positivos A y B. hallar el mayor de los dos numeros.
#Ej: A=12, B=7. resultado: MAY=12 (sin utilizar [If])
#solicitamos al usuario dos numeros:
A = int(input("ingrese el valor de A: "))
B = int(input("ingrese el valor de B: "))
#realizamos las operaciones aritmeticas basicas para encontrar el mayor:
sum = A + B
res = abs(A - B) #la palabra [abs] significa el valor absoluto
#a los resultados de suma y resta le sumamos a una variable
sumR= sum + res
#luego de obtener la variable,  le dividimos para obtener el mayor
div= sumR / 2
#mostramos por pantalla el resultado final.
print(f"numeros elegidos son {A} y {B}, el mayor es: {div}")