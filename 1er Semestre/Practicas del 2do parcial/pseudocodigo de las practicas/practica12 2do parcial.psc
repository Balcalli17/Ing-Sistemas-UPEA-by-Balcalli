Algoritmo notasexamen
	Escribir "ingrese nota del estudiante: "
	Leer nota
	Si nota<51 Entonces
		Escribir "nota mala"
	SiNo
		Si nota>=51 y nota<65 Entonces
			Escribir "nota regular"
		SiNo
			Si nota>=65 y nota<80 Entonces
				Escribir "nota buena"
			SiNo
				Si nota>=80 y nota<90 Entonces
					Escribir "nota muy buena"
				SiNo
					Si nota>=90 y nota<=100 Entonces
						Escribir "nota excelente"
					SiNo
						Escribir "ingrese nota nuevamente"
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
