def int_func(a):
    str_res = a.capitalize() + " "
    for i in range(0, len(a)):
        if ord(a[i]) >= 97 and ord(a[i]) <= 122:
            continue
        else:
            str_res = ""
            break
    return str_res


a = input("Введите слова: ").split()
res = ""
for i in a:
    res = res + str(int_func(i))
print(res)
