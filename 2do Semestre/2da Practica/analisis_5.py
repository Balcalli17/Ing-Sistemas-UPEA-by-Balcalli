import random
import time

#metodo de ordenacion
def insertionSort(V,n):
	i=1
	while i < n:
		actual=V[i]
		j=i-1
		while j >=0 and V[j] > actual:
			V[j+1]= V[j]
			j-=1
		V[j+1]=actual
		i+=1

# Búsqueda Binaria
def busq_binaria(V,n,x):
	izq = 0
	der = n - 1
	encontrado = False

	while izq <= der and not encontrado:
		medio = (izq + der) // 2
		if V[medio] == x:
			encontrado = True
		elif x < V[medio]:
			der = medio - 1
		else:
			izq = medio + 1
	return busq_binaria
        	
def main():
	while True:
		try:
			n=int(input("Ingrese tamañon de vector: "))
			if(n>0):
				break
			else:
				print("el numero es negativo")
		except ValuesError:
			print("error...")
		
	V=[random.randint(0,100) for i in range(n)]
	insertionSort(V,n)
	print("V= ",V)
	x = int(input("Ingrese el número a buscar (0 - 100): "))
	inicio=time.time()
	if busq_binaria(V,n,x):
		print("el numero fue encontrado...")
		fin=time.time()
		tiempo=fin-inicio
		print(f"Tiempo transcurrido: {tiempo} segundos " )
		print("Complejidad algoritmica mejor de los casos: O(1)")
	else:
		print("no se encontro el numero")
	
main()
