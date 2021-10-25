def exp(x, y):
    res = x ** y
    print(res)


x = 0
y = 0
while x <= 0:
    try:
        x = float(input("Введите действительное положительное число "))
    except:
        continue

while y >= 0:
    try:
        y = int(input("Введите целое отрицательное число"))
    except:
        print("Число должно быть целым!")

exp(x, y)
