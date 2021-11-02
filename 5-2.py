with open("task1.txt", "r", encoding="utf-8") as f:
    line_count = 0
    for line in f:
        line_count += 1
        word_count = len(line.split())
        print(f"Строка {line_count} - слов {word_count}")
    print(f"Всего строк в файле: {line_count}")
