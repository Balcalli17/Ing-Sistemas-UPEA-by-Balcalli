"""
18.Realiza una función que reciba una cadena reemplace las vocales por números del 1 al 5.
ej :ENTRADA: ingrese la cadena: SISTEMAS ,SALIDA: S3ST2M1S 
"""
#FUNCIONES:
def reemplazar_vocales(cadena):
    # Variable donde construiremos la nueva cadena
    resultado = ""
    
    # Recorremos caracter por caracter
    for caracter in cadena:
        # Comprobamos cada vocal (mayúscula y minúscula)
        if caracter == 'a' or caracter == 'A':
            resultado = resultado + "1"
        elif caracter == 'e' or caracter == 'E':
            resultado = resultado + "2"
        elif caracter == 'i' or caracter == 'I':
            resultado = resultado + "3"
        elif caracter == 'o' or caracter == 'O':
            resultado = resultado + "4"
        elif caracter == 'u' or caracter == 'U':
            resultado = resultado + "5"
        else:
            # Si no es vocal, lo dejamos igual
            resultado = resultado + caracter
    
    return resultado

#PRINCIPAL:
def main():
    texto = input("Ingrese la cadena: ")
    print("Cadena transformada:", reemplazar_vocales(texto))
main()
