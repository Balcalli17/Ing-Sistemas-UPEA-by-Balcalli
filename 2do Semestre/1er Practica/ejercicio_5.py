#funcion factorial
def sum_acum(a):
	s=0
	for i in range (1,a+1):
		s=s+((i*(i+1))//2)
	return s
	
def main():
	while (True):
		n=int(input("ingrese el numero de terminos: "))
		if(n>0):
			break
	s=sum_acum(n)
	print(f"ls suma es : {s}")
	
#prog. principal
main()