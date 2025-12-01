while(True):
    print("selecione el tipo de figura: ")
    print("1.rectangulo")
    print("2.cuadrado")
    print("3.triangulo")
    print("0.salir")
    tipo_de_figura = input("ingrese una opcion: ")

    if tipo_de_figura == "0":
        print("fin del programa")
        break

    else:
        if tipo_de_figura == "1":
            base = int(input("ingrese la base del rectangulo: "))
            altura = int(input("ingrese la altura del rectangulo: "))
            area = base * altura
            perimetro = 2*(base + altura)
            print(f"area del rectangulo es: {area}")
            print(f"perimetro del rectangulo es : {perimetro}")
            
        else:
            if tipo_de_figura == "2":
                lado = int(input("ingrese lado del cuadrado:"))
                area = lado * lado
                perimetro = 4 * lado
                print(f"area del cuadrado: {area}")
                print(f"perimetro del cuadrado: {perimetro}")

            else:
                if tipo_de_figura == "3":
                    base = int(input("ingrese la base del triangulo: "))
                    altura = int(input("ingrese la altura del triangulo: "))
                    lado1 = int(input("ingrese lado 1 del triangulo: "))
                    lado2 = int(input("ingrese lado 2 del triangulo: "))
                    area = (base*altura)/2
                    perimetro = base + lado1 + lado2
                    print(f"area del triangulo: {area}")
                    print(f"perimetro del triangulo: {perimetro}")

                else:
                    print("opcion no valida.")

