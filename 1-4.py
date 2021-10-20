n = int(input("Введите число: "))
nmax = 0
while n > 0:
    num = n % 10
    if nmax >= num:
        pass
    else:
        nmax = num
    n = n // 10
print(f"Максимальная цифра в числе {nmax}")
