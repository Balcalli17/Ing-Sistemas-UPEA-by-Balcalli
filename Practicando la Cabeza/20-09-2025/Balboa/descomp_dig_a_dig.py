#suma de dos numeros enteros digito a digito:
#FUNCIONES
def suma_dig_dig(a,b):
    p = 1
    ac = 0
    s = 0
    while a>0 or b>0:
        da = a % 10
        db = b % 10
        aux = da + db + ac
        r1 = aux % 10
        r2 = aux // 10
        s = r1 * p + s
        ac = r2
        p = p * 10
        a = a // 10
        b = b // 10
    if ac == 1:
        s =r2 * p + s
    return s

#PRINCIPAL
def main():
    a = int(input("ingrese valor de a: "))
    b = int(input("ingrese valor de b: "))
    s = suma_dig_dig(a,b)
    print(f"{a}+{b}={s}")
main()