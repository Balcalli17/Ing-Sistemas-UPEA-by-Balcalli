#funcion factorial
def factorial(a):
	f=1
	for i in range (1,a+1):
		f*=i
	return f
#funcion combinacion
def combinacion(a,b):
	c=factorial(a)//(factorial(a-b)*factorial(b))
	return c
	
def main():
	while (True):
		n=int(input("ingrese n: "))
		r=int(input("ingrese r: "))
		if(n>0 and r>0):
			break
	c=combinacion(n,r)
	print(c)
	
#prog. principal
main()