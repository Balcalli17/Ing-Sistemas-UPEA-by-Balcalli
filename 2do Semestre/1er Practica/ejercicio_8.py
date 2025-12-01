#Realice las funciones necesarias para generar los n terminos de las siguientes series:
#N = 5
#a = 1,1,0,1,1   b = 3,4,7,11,18
#FUNCIONES:
def serie_a(n):
	for i in range (1,n+1):
		if(i%3==0):
			print("0,",end="")
		else:
			print("1,",end="")
def serie_b(n):
	serie=3
	aux=0
	inc=1
	for i in range(n):
		print(f"{serie},",end="")
		aux=serie
		serie=aux+inc
		inc=aux
#PRINCIPAL:		
def main():
	while True:
		n=int(input("N: "))
		if(n>0):
			break
	serie_a(n)
	print("")
	serie_b(n)
main()