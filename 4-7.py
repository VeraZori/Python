n = int(input("Введите n: "))


def fact(n):
    res = 1
    for el in range(1, n + 1):
        res *= el
        yield el
    print(res)


for el in fact(n):
    print(el)
fact(n)
