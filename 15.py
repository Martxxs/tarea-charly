description="Aqui imprimiremos una lista de numeros,pares e inpares por favor ponga un limite"
print(f"{description}\n")
n=input("introdusca su limite: ")
def generar_lista(n):
    lista = []
    i = 1
    while i <= n:
        lista.append(i)
        i += 1
    return lista
n = int(n) 
numeros = generar_lista(n)
print(numeros)
pares = [x for x in numeros if x % 2 != 1]
print(pares)  
impares = [x for x in numeros if x % 2 != 0]
print(impares) 