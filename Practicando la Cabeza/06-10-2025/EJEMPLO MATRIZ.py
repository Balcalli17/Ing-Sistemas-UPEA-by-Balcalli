"""
1.generamos una matriz M de tamaño NxM:
[ 1  , 2  , 3  , 4  ]
[ 5  , 6  , 7  , 8  ]
[ 9  , 10 , 11 , 12 ]
[ 13 , 14 , 15 , 16 ] 
"""
fil=int(input("ingrese tamaño de fila: "))
col=int(input("ingrese tamaño de columna: "))
matriz = [[0]*col for _ in range(fil)]
c = 1
for i in range(0,fil):
    for j in range(0,col):
        matriz[i][j]=c
        c = c + 1

for i in range(0,fil):
    for j in range(0,col):
        print(matriz[i][j],end="\t")
    print("")