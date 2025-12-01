def area_cuadrado(lado):
	a=lado*lado
	return a
	
def peri_cuadrado(lado):
	p=lado*4
	return p

def main():
	while (True):
		n=int(input("ingrese el valor de un lado: "))
		if n>0:
			break
	area=area_cuadrado(n)
	per=peri_cuadrado(n)
	print(f"el area es : {area}")
	print(f"el perimetro es: {per}")

#programa principal
main()
	