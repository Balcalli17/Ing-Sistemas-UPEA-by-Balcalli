"""
5.Realice que una función para leer N elementos enteros en un vector, 
luego retornar el mismo vector con sus elementos segundo y penúltimo intercambiados.
"""
#FUNCIONES:
def llenar_vector(v,n):
	for i in range (n):
		v[i]=int(input(f"V[{i}]= "))
def mostrar_vector(v,n):
	print("V= ",v)
def nuevo_vector(v,n):
	for i in range (n):
		if i==1:
			aux=v[i]
			v[i]=v[n-2]
			v[n-2]=aux
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
	nuevo_vector(v,n)
	mostrar_vector(v,n)
main()