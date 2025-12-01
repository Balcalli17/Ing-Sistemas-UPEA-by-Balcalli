Algoritmo practica4
	Repetir
		Escribir "ingrese el tipo de figura (1-rectangulo, 2-cuadrado ,3-triangulo ,0-salir):"
		Leer tipodefigura
		Si tipodefigura = 1 Entonces
			Escribir "ingrese base del rectangulo:"
			Leer base
			Escribir "ingrese la altura del rectangulo:"
			Leer altura
			area <- base * altura
			perimetro <- 2*(base + altura)
			Escribir "area del rectangulo:",area
			Escribir "perimetro del rectangulo:",perimetro
		SiNo
			Si tipodefigura = 2 Entonces
				Escribir "ingrese lado del cuadrado:"
				Leer lado
				area <- lado * lado
				perimetro <- 4 * lado
				Escribir "area del cuadrado:", area
				Escribir "perimetro del cuadrado:", perimetro
			SiNo
				Si tipodefigura = 3 Entonces
					Escribir "ingrese la base del triangulo:"
					Leer base
					Escribir "ingrese la altura del triangulo:"
					Leer altura
					Escribir "ingrese lado 1 del triangulo:"
					Leer lado1
					Escribir "ingrese lado 2 del triangulo:"
					Leer lado2
					area <- (base*altura)/2
					perimetro <- base + lado1 + lado2
					Escribir "area del triangulo:",area
					Escribir "perimetro del triangulo:",perimetro
				SiNo
					Si tipodefigura<>0 Entonces
						Escribir "opcion no valida"
					SiNo
						
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Hasta Que tipodefigura = 0
	
	Escribir "fin del programa"
FinAlgoritmo
