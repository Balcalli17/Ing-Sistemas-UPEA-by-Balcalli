Proceso BuscarSubnumeros
    Definir A, B, C Como Entero
    Definir strA, strB, strC Como Cadena
	
    Escribir "Ingrese el número A: "
    Leer A
	
    Escribir "Ingrese el número B: "
    Leer B
	
    Escribir "Ingrese el número C: "
    Leer C
	
    strA <- ConvertirATexto(A)
    strB <- ConvertirATexto(B)
    strC <- ConvertirATexto(C)
	
		Si SubCadena(strA, strB) <> -1 Entonces
			Escribir "El número ", B, " se encuentra en el número ", A
		FinSi
		
			Si SubCadena(strA, strC) <> -1 Entonces
				Escribir "El número ", C, " se encuentra en el número ", A
			FinSi
FinProceso
