"""
20.Realiza una función que reciba una palabra y desplace cada letra una cantidad n de posiciones.
ej: ENTRADA: palabra = hola, SALIDA: nueva palabra = jqnc
             n = 2
"""
#FUNCIONES:
def desplazar_palabra(palabra, n):
    # Abecedario (minúsculas)
    abecedario = "abcdefghijklmnopqrstuvwxyz"
    resultado = ""
    # Recorremos cada letra de la palabra
    for letra in palabra:
        # Buscar posición de la letra en el abecedario
        posicion = -1
        for i in range(26):  # hay 26 letras
            if letra == abecedario[i]:
                posicion = i
                break
        # Si encontramos la posición, desplazamos
        if posicion != -1:
            nueva_pos = posicion + n
            # Ajustar si pasa del final
            if nueva_pos >= 26:
                nueva_pos = nueva_pos - 26
            # Concatenamos la letra desplazada
            resultado = resultado + abecedario[nueva_pos]
        else:
            # Si no está en el abecedario (ej: espacio), se deja igual
            resultado = resultado + letra
    return resultado
#PRINCIPAL:
def main():
    pal = input("Ingrese la palabra: ")
    n = int(input("Ingrese el valor de n: "))
    print("Nueva palabra:", desplazar_palabra(pal, n))
main()