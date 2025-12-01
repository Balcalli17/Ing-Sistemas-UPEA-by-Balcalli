"""
6.Escribe un programa que, al dar como dato un arreglo unidimensional de números enteros, 
determine cuántos de ellos son positivos, cuántos negativos y cuántos nulos.
"""
#fUNCIONES:
def llenar_vector(v,n):
	print("dame elementos del vector: ")
	for i in range (n):
		v[i]=int(input(f"V[{i}]= "))
def mostrar_vector(v,n):
	print("V= ",v)
def barrido_vector(v,n):
	pos=0
	nul=0
	neg=0
	for i in range (n):
		if v[i] > 0:
			pos=pos+1
		else:
			if v[i] ==0:
				nul=nul+1
			else:
				neg=neg+1
	print("Positivos: ",pos)
	print("negativos: ",neg)
	print("nulos: ",nul)
#PRINCIPAL:	
def main():
	while True:
		try:
			n=int(input("ingrese el tamaño del vector: "))
			if(n>0):
				break
			else:
				print("el numero es negativo")
		except ValueError:
			print("error....")
	v=[0]*n
	llenar_vector(v,n)
	mostrar_vector(v,n)
	barrido_vector(v,n)
main()