import random
def buscar_x(V,n):
	x=int(input("\nIngrese x : "))
	for i in range(n):
		if x==V[i]:
			print(i,end=",")
			
def Mostrar_vector(V,n):
	print("V = ",V)
	
def main():
	while True:
		try:
			n=int(input("ingrese tamaño del vector : "))
			if n>0:
				break
			else:
				print("el numero es negativo")
		except ValuesError:
			print("error...!!!")
	V=[random.randint(0,10) for i in range(n)]
	Mostrar_vector(V,n)
	buscar_x(V,n)
	
main()