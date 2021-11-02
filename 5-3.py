with open("samples/text_3.txt", "r", encoding="utf-8") as f:
    count_pers = 0
    av_sal = 0
    for line in f:
        count_pers += 1
        line = line.split()
        av_sal = av_sal + float(line[1])
        if float(line[1]) < 20000.00:
            print(line[0])
av_sal = av_sal / count_pers
print(f"Средняя величина дохода {av_sal}")
