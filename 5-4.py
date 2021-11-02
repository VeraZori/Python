change = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new = []
with open("samples/text_4.txt", "r", encoding='utf-8') as f:
    for line in f:
        line = line.split(" ", 1)
        new.append(change[line[0]] + " " + line[1])
    print(new)
with open("task4.txt", "w", encoding='utf-8') as f:
    f.writelines(new)
