import random

def buscar_menor(V,n):
	menor =999999
	for i in range(n):
		if V[i]<menor:
			menor=V[i]
			lim=i
#reordenamos vector	
	for i in range(lim,0,-1):
		V[i] = V[i-1]
	V[0]=menor
	
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
	V=[random.randint(0,100) for i in range(n)]
	Mostrar_vector(V,n)
	print("\nNuevo vector ordenado")
	buscar_menor(V,n)
	Mostrar_vector(V,n)
	
main()