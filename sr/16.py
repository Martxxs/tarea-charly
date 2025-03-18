def factorial(n):
    if n < 0:
        return " no está definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        i = 2
        while i <= n:
            resultado *= i
            i += 1
        return resultado

# Solicitar al usuario un número
num = int(input("Ingrese un número: "))
print(f"El factorial de {num}{factorial(num)}")
