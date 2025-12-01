#formas para imprimir texto
nombre = "Mari cruz"
edad = 24
peso = 62.7
"""
ESPECIFICADOR DE TIPO:
%s = cadena
%d = entero
%f = float
"""
print("Mi nombre es %s, tengo %d años, peso %.2f" % (nombre,edad,peso))
print("Mi nombre es %s," % (nombre),end="")
print(" tengo %d años," % (edad),end="")
print(" peso %.2f" % (peso))
#--------------------------------------------------------------------------------------
A = 4
B = 7
C = A + B
print("la suma de %d + %d = %d" % (A,B,C))
#otra forma de realizarlo...
print("la suma de %d + %d = %d" % (A,B,A+B))