Algoritmo  ClasificarNumero
    Definir numero Como Entero
    Definir signo Como Cadena
    Definir paridad Como Cadena
    
    Escribir "Ingrese un número entero:"
    Leer numero
    
    // Determinar el signo del número
    Si numero > 0 Entonces
        signo <- "positivo"
    Sino
        Si numero < 0 Entonces
            signo <- "negativo"
        Sino
            signo <- "cero"
        FinSi
    FinSi
    
    // Determinar si es par o impar (solo si no es cero)
    Si numero <> 0 Entonces
        Si numero % 2 == 0 Entonces
            paridad <- "par"
        Sino
            paridad <- "impar"
        FinSi
    Sino
        paridad <- "no aplica (cero no es par ni impar)"
    FinSi
    
    // Mostrar el resultado
    Escribir "El número ", numero, " es ", signo, " y es ", paridad, "."
FinAlgoritmo
