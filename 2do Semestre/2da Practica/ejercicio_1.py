def llenar_vector(V,n):
	for i in range(n):
		V[i]=int(input(f"V[{i}]= "))
def mostrar_vector(V,n):
	print("V = ",V)
	
def buble_ascendente(V,lim):
	for i in range(lim):
			for j in range (lim-1):
				if (V[j]>V[j+1]):
					aux=V[j]
					V[j]=V[j+1]
					V[j+1]=aux
	return V
	
def buble_descendente(V,mitad,n):
	for i in range(mitad,n,1):
		for j in range(mitad,n-1):
			if (V[j]<V[j+1]):
				aux=V[j]
				V[j]=V[j+1]
				V[j+1]=aux
	return V
			
def nuevo_vector(V,n):
	if n%2==0:
		mitad=n//2
		buble_ascendente(V,mitad)
		buble_descendente(V,mitad,n)
	else:
		mitad=(n//2+1)
		buble_ascendente(V,mitad)
		buble_descendente(V,mitad,n)
		
def main():
	while True:
		try:
			n=int(input("Ingrese tamañon del vector: "))
			if(n>0):
				break
			else:
				print("el numero es negativo")
		except ValuesError:
			print("error...")
		
	V=[0]*n
	llenar_vector(V,n)
	mostrar_vector(V,n)
	nuevo_vector(V,n)
	print("Nuevo vector:")
	mostrar_vector(V,n)
main()