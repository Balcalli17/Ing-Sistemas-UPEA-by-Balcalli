dia = input("ingrese un dia de la semana: ")

if dia == "lunes":
    categoria = "inicio de semana"
else:
    if dia == "martes" or dia == "miercoles" or dia == "jueves":
        categoria = "mediados de semana"
    else:
        if dia == "viernes":
            categoria = "inicio de fin de semana"
        else:
            if dia == "sabado" or dia == "domingo":
                categoria = "fin de semana"
            else:
                categoria = "dia no valido, ingrese nuevamente"
                
print(f"dia ingresado es: {dia}")
print(f"corresponde a la semana: {categoria}")