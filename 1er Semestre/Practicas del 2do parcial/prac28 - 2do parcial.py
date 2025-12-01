#ejercicio 28: programa que permite introducir N
#por teclado, obteniendo el factorial de los pares y la sumatoriade los impares

n =  int(input("ingrese cuantos numeros vas a solicitar: "))
sum_impar = 0
for i in range (0,n):
    num = int(input("ingrese los numeros: "))
    
    if num % 2 == 0:
        fact = 1
        for j in range (1,num+1):
            fact = fact * j
        print("el factorial de", num ,  "es: ", fact)
    else:
        sum_impar = sum_impar + num
        
print(f"la suma de los numeros impares es: {sum_impar}")