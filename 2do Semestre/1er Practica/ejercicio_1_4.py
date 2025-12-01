"""
4.Leer un vector con N elementos enteros, retornar una copia con los elementos en orden inverso.
"""
#FUNCIONES:
def crearv(v,n):
	for i in range (n):
		v[i]=int(input(f"V[{i}]= "))
def imprimirv(v,n):
	print("V= ",v)
def invertir_vector(v2,v,n):
	d=n-1
	for i in range (n):
		v2[d]=v[i]
		d=d-1
#PRINCIPAL:
def main():
	while True:
		try:
			n=int(input("ingrese tamaño del vector: "))
			if(n>0):
				break
			else:
				print("el numero es negativo")
		except ValueError:
			print("error....")
	v=[0]*n
	v2=[0]*n
	crearv(v,n)
	imprimirv(v,n)
	invertir_vector(v2,v,n)
	imprimirv(v2,n)
main()