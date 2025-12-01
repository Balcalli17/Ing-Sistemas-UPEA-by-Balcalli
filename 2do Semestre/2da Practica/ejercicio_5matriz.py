def llenar_matriz(M,n):
	for i in range (n):
		for j in range(n):
			M[i][j]=int(input(f"M[{i}][{j}] = "))
def  busqueda_matriz(M,n):
	for i in range (n):
		mayor=0
		for j in range(n):
			if (M[i][j]>mayor):
				mayor=M[i][j]
		print(f"El mayor de la col {i} es : ",mayor)
def mostrar_matriz(M,n):
	for i in range(n):
		for j in range(n):
			print(M[i][j],end="   ")
		print("")
	
def main():
	while True:
		try:
			n=int(input("Ingrese dimension de matriz: "))
			if(n>0):
				break
			else:
				print("El numero ingresado es negativo")
		except ValuesError:
			print("Error...")
	M=[[0]*n for i in range (n)]
	llenar_matriz(M,n)
	mostrar_matriz(M,n)
	busqueda_matriz(M,n)
main()