def es_primo(numero):
    if numero <= 1:
        return False
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            return False
        i += 1
    return True
numero = int(input("Introduce un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")