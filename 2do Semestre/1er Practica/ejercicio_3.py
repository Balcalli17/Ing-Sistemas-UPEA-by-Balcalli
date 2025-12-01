def factorial(num):
	f=1
	for i in range(1,num+1):
		f=f*i
	return f
	
def resta(a,b):
	r=a-b
	return r
	
def division (a,b):
	d=a//b
	return d
	
def main():
	p=0
	while (True):
		n=int(input("ingrese n: "))
		r=int(input("ingrese r: "))
		if(n>0 and r>0):
			break
	p=division(factorial(n),factorial(resta(n,r)))
	print(p)
	
main()