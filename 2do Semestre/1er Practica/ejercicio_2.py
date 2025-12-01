def area_circulo(radio):
	pi=3.1416
	a=pi*(radio*radio)
	return a
	
def peri_circulo(radio):
	pi=3.1416
	p=2*pi*radio
	return p

def main():
	while (True):
		n=int(input("ingrese el valor del radio: "))
		if n>0:
			break
	area=area_circulo(n)
	per=peri_circulo(n)
	print(f"el area es : {area:.2f}")
	print(f"el perimetro es: {per:.3f}")

#programa principal
main()
	