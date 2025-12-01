def generar_matriz(M,n):
	for i in range (n):
		for j in range(n):
			M[i][j]=0
	for i in range (n):
		for j in range(n):
			M[j][0]=1
			M[j][n-1]=1
			if i==j:
				M[i][j]=1
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