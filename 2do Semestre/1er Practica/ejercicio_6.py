#Realice las funciones necesarias, para obtener el resultado de la siguiente ecuacion:
#res = raiz(a**3+b**3+c**3)
#FUNCIONES:
def cubo(num):
	c=num*num*num
	return c

def raiz_cuadrada(num):
	aproximacion =num/2.0
	for i in range(20):
		aproximacion = (aproximacion + num / aproximacion) / 2.0
	return aproximacion

#PRINCIPAL:
def main():
	while True:
		a=int(input("Introduzca un numero a: "))
		b=int(input("Inteoduzca un numero b: "))
		c=int(input("Inteoduzca un numero b: "))
		if(a>=0 and b>=0 and c>=0):
			break
	r=raiz_cuadrada(cubo(a)+cubo(b)+cubo(c))
	print(f"Res= {r:.6}")
	
main()
