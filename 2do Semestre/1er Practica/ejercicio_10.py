#Realice las funciones necesarias, para calcular el valor de aproximado de "pi" (serie de leibniz), segun la serie:
#pi = +4/1-4/3+4/5-4/7+4/9-... 
#n = 5    resultado = 3.3396
#FUNCIONES:
def serie_leibniz(num):
	pi=0
	inc=1
	for i in range(1,num+1):
		if(i%2==0):	
			pi=pi-(4/inc)
		else:
			pi=pi+(4/inc)
		inc=inc+2
	return pi
		
#PRINCIPAL:
def main():
	while True:
		n=int(input("Introduzca N: "))
		if n>0:
			break
	pi=serie_leibniz(n)
	print(f"Resultado: {pi:.5}")
	
main()