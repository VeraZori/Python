import re

with open("samples/text_6.txt", "r", encoding="utf-8") as f:
    res = {}
    for i in f:
        subj, lect, pract, lab = i.split()
        lect = re.findall(r"\d+", lect)
        lect = [int(el) for el in lect]
        pract = re.findall(r"\d+", pract)
        pract = [int(el) for el in pract]
        lab = re.findall(r"\d+", lab)
        lab = [int(el) for el in lab]
        sum_subj = sum(lect + pract + lab)
        res[subj] = sum_subj

    print(res)
