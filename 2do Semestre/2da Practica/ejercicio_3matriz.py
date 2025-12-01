def generar_matriz(M,n):
	for i in range (n):
		for j in range(n):
			M[i][j]=0
	if n%2== 0:
		mitad=n//2
		for i in range (n):
			for j in range(mitad):
				if i==j:
					M[i][j]=j+1
		for i in range (n):
			for j in range(mitad,n):
				if(i+j==n-1):
					M[i][j]=j+1
	else:
		mitad=n//2+1
		for i in range (n):
			for j in range(mitad):
				if i==j:
					M[i][j]=j+1
		for i in range (n):
			for j in range(mitad,n):
				if(i+j==n-1):
					M[i][j]=j+1
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
	generar_matriz(M,n)
	mostrar_matriz(M,n)
main()