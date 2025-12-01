Algoritmo diadesemana
	Escribir "ingrese un dia de la semana: "
	Leer dia
	Si dia = "lunes" Entonces
		categoria = "inicio de semana"
	SiNo
		Si dia = "martes" o dia = "miercoles" o dia = "jueves" Entonces
			categoria = "mediados de semana"
		SiNo
			Si dia = "viernes" Entonces
				categoria = "inicio de fin de semana"
			SiNo
				Si dia = "sabado" o dia = "domingo" Entonces
					categoria = "fin de semana"
				SiNo
					categoria = "dia no valido, ingrese nuevamente"
				Fin Si
			Fin Si
		Fin Si
	Fin Si
	Escribir "dia ingresado :",dia
	Escribir "corresponde a: ",categoria
FinAlgoritmo
