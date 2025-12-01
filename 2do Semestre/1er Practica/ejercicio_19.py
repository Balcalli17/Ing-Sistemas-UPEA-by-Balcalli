"""
19.Realiza una función que calcule la edad de un individuo a partir de la fecha de nacimiento.
ej: ENTRADA: fecha = 03/05/2005 ,SALIDA: edad = 20
"""
#FUNCIONES:
def verif_edad(dia,mes,año,diaactual,mesactual,añoactual):
    edad=0
    if año <= añoactual:
        edad = añoactual - año
    else:
        if mes <= mesactual:
            edad=añoactual - año
        else:
            if dia <= diaactual:
                edad=añoactual - año
    return edad
#PRINCIPAL:
def main():
    print("fecha de nacimiento:")
    dia = int(input("ingrese el dia de la fecha de nacimiento: "))
    mes = int(input("ingrese el mes de la fecha de nacimiento: "))
    año = int(input("ingrese el año de la fecha de nacimiento: "))
    print("fecha actual:")
    diaactual=int(input("ingrese el dia de la fecha actual: "))
    mesactual=int(input("ingrese el dia de la fecha actual: "))
    añoactual=int(input("ingrese el dia de la fecha actual: "))

    res = verif_edad(dia,mes,año,diaactual,mesactual,añoactual)
    print(res)
main()