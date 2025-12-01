def llenar_matriz(M,n,m):
	for i in range (m):
		for j in range(n):
			M[i][j]=int(input(f"M[{i}][{j}] = "))
def orden_ascendente(M,n,m):
	for i in range (m):
		if ((i)%2==0):
			for j in range (n):
				for k in range (n-1):
					if M[i][k]>M[i][k+1]:
						aux=M[i][k]
						M[i][k] =M[i][k+1]
						M[i][k+1]=aux
		else:
			for j in range (n):
				for k in range (n-1):
					if M[i][k]<M[i][k+1]:
						aux=M[i][k]
						M[i][k] =M[i][k+1]
						M[i][k+1]=aux		
						

def mostrar_matriz(M,n,m):
	for i in range(m):
		for j in range(n):
			print(M[i][j],end="   ")
		print("")
	
def main():
	while True:
		try:
			m=int(input("Ingrese dimension m fila de matriz: "))
			n=int(input("Ingrese dimension n columnade matriz: "))
			if(m>0 and n>0):
				break
			else:
				print("El numero ingresado es negativo")
		except ValuesError:
			print("Error...")
	M=[[0]*n for i in range (m)]
	llenar_matriz(M,n,m)
	mostrar_matriz(M,n,m)
	orden_ascendente(M,n,m)
	print("Nueva Matriz :")
	mostrar_matriz(M,n,m)
main()