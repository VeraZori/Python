my_list = input("Введите элементы списка через пробел: ").split()
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print("Преобразованный список: "+" ".join([str(i) for i in my_list]))

