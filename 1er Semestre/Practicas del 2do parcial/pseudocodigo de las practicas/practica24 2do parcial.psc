Algoritmo  Digitos_Comunes
	
    Definir num1, num2, dig1_1, dig1_2, dig2_1, dig2_2 Como Entero
	
    Escribir "Ingrese el primer número de dos dígitos: "
    Leer num1
	
    Escribir "Ingrese el segundo número de dos dígitos: "
    Leer num2
	
    Si (num1 >= 10 Y num1 <= 99) Y (num2 >= 10 Y num2 <= 99) Entonces
		
        dig1_1 <- num1 / 10
        dig1_2 <- num1 % 10
		
        dig2_1 <- num2 / 10
        dig2_2 <- num2 % 10
		
        Si dig1_1 = dig2_1 O dig1_1 = dig2_2 O dig1_2 = dig2_1 O dig1_2 = dig2_2 Entonces
            Escribir "Los números tienen al menos un dígito en común."
        Sino
            Escribir "Los números NO tienen dígitos en común."
        FinSi
		
    Sino
        Escribir "Error: ambos números deben tener dos dígitos (entre 10 y 99)."
    FinSi

FinAlgoritmo

