def contar_letras(palabra):
    palabra = palabra.replace(" ", "").lower()
    conteo = {}
    for letra in palabra:
        if letra in conteo:
            conteo[letra] += 1
        else:
            conteo[letra] = 1
    return conteo

def anagrama(a, b):
    return contar_letras(a) == contar_letras(b)

x = input("Ingrese la primera palabra: ")
y = input("Ingrese la segunda palabra: ")

if anagrama(x, y):
    print("Las palabras son anagramas.")
else:
    print("Las palabras NO son anagramas.")
