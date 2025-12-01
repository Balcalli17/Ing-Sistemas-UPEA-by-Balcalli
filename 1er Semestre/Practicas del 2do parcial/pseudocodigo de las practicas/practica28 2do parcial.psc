Algoritmo  Factorial_Pares_Suma_Impares
	
    Definir n, i, numero, j, factorial, sum_impar Como Entero
    sum_impar <- 0
	
    Escribir "ingrese cuantos numeros vas a solicitar: "
    Leer n
	
    Para i <- 1 Hasta n Con Paso 1
        Escribir "Ingresa un número:"
        Leer numero
		
        Si numero % 2 = 0 Entonces
            factorial <- 1
            Para j <- 1 Hasta numero Con Paso 1
                factorial <- factorial * j
            FinPara
            Escribir "El factorial de ", numero, " es ", factorial
        Sino
            sum_impar <- sum_impar + numero
        FinSi
    FinPara
	
    Escribir "La suma de los números impares es: ", sum_impar
	
FinAlgoritmo

