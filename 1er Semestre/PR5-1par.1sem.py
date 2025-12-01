#5. Obtenga la cantidad de ladrillos que se necesitan para armar una pared dada la longitud y altura de la pared, considerando que se emplean 116 ladrillos comunes en 2 m2.
#solicitamos por pantalla, la altura y longitud de la pared.
longitud=float(input("ingrese la longitud de la pared (en metros): "))
altura=float(input("ingrese la altura de la pared (en metros): "))
#creamos una variable para este ejercicio.
m2 = 116 #por cada 2x2 metros de la pared, se necesita 116 ladrillos.
#hallamos el area de una pared y guardamos en una variable el resultado.
sum_lon_y_altura = longitud*altura
#creamos la condicion del anterior operacion y formulamos el resultado final.
variable = sum_lon_y_altura/2
ladrillos_necesarios = variable * m2
#mostramos por pantalla el resultado, la cantidad de ladrillos necesaria para la pared.
print(f"los ladrillos necesarios para la pared son: {ladrillos_necesarios}")
