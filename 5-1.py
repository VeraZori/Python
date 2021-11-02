with open("task1.txt", "w", encoding="utf-8") as f:
    while str != "":
        str = input("Введите данные: ")
        f.write(f"{str}\n")
