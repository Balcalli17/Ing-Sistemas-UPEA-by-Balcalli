nota = int(input("ingrese nota del estudiante: "))

if nota < 51:
    print("nota mala")
elif nota >= 51 and nota < 65:
    print("nota regular")
elif nota >= 65 and nota < 80:
    print("nota buena")
elif nota >= 80 and nota < 90:
    print("nota muy buena")
elif nota >= 90 and nota <= 100:
    print("nota excelente")