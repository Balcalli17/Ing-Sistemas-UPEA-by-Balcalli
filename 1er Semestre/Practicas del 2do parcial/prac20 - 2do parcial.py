A = int(input("ingrese el numero A: "))
B = int(input("ingrese el numero B: "))
C = int(input("ingrese el numero C: "))

str_A= str(A)
str_B= str(B)
str_C= str(C)

if str_B in str_A:
    print(f"el numero {B} se encuentra en numero {A}")
if str_C in str_A:
    print(f"el numero {C} se encuentra en numero {A}")