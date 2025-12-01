Proceso OperacionesMat
    Definir num1, num2, resultado Como Real
    Definir operacion Como Caracter
	
    Escribir "Ingrese el primer número: "
    Leer num1
	
    Escribir "Ingrese el segundo número: "
    Leer num2
	
    Escribir "Ingrese la operación a realizar (S: Suma, R: Resta, M: Multiplicación, D: División): "
    Leer operacion
	
    Segun operacion Hacer
        'S':
            resultado <- num1 + num2
            Escribir "El resultado de la suma es: ", resultado
        'R':
            resultado <- num1 - num2
            Escribir "El resultado de la resta es: ", resultado
        'M':
            resultado <- num1 * num2
            Escribir "El resultado de la multiplicación es: ", resultado
        'D':
            Si num2 = 0 Entonces
                Escribir "Error: No se puede dividir por cero."
            Sino
                resultado <- num1 / num2
                Escribir "El resultado de la división es: ", resultado
            FinSi
        De Otro Modo:
            Escribir "Operación no válida."
    FinSegun
FinProceso
