def fib(n):
    x, y = 0, 1
    res = []
    while x <= n:
        res.append(x)
        x, y = y, x + y
    return res

num = int(input("Número: "))
print(fib(num))
