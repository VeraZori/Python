with open("task5.txt", "w", encoding="utf-8") as f:
    num = input("Введите числа через пробел")
    f.write(num)

with open("task5.txt", "r", encoding="utf-8") as f:
    num = f.read()
    num = num.split()
    print(sum(map(int, num)))
