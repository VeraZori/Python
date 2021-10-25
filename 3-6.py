def int_func(a):
    str_res = a.capitalize()
    for i in range(0, len(a)):
        if ord(a[i]) >= 97 and ord(a[i]) <= 122:
            continue
        else:
            str_res = ("строка содержит не латинские буквы или прописные буквы")
            break
    return str_res


a = input("Введите слово: ")

print(int_func(a))
