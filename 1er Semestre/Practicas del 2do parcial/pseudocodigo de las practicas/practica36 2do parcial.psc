Algoritmo generar_serie
    Definir N, i, termino Como Entero;
    
    Escribir "Ingrese el número de términos (N): ";
    Leer N;
    
    termino <- 1;
    
    Escribir "Sucesión generada: " Sin Saltar;
    
    Para i <- 1 Hasta N Hacer
        Si i % 2 == 1 Entonces
            termino <- (i + 1) / 2;
        Sino
            termino <- i + (i / 2);
        FinSi
        
        Escribir termino Sin Saltar;
        
        Si i < N Entonces
            Escribir ", " Sin Saltar;
        FinSi
    FinPara
    
    Escribir ""; // Salto de línea final
FinAlgoritmo
