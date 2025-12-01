import random
n = int(input("cuantos numeros quieres ingresar a la pantalla: "))
for i in range(n):
    num = random.randint(1,10)
    print(num,end="-")
"""
para trabajar con numeros extension (y tambien aleatorio) se importa de una libreria el comando
"import random" luego le asignamos a una variable cualquiera el siguiente codigo
*ej: "num = random.randint(1,10)" donde "(1,10)" significa "(numero donde incia,donde termina)"
"""