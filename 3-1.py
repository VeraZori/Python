def div(a, b):
    try:
        res = a / b
        print(res)
    except ZeroDivisionError:
        print("Второе число не может быть 0")


a = float(input("Введите число: "))
b = float(input("Введите число: "))
div(a, b)
