def my_func(a, b, c):
    d = min(a, b, c)
    res = a + b + c - d
    print(f"Сумма двух наибольших чисел: {res}")


a = int(input("Введите число 1 "))
b = int(input("Введите число 2 "))
c = int(input("Введите число 3 "))
my_func(a, b, c)
