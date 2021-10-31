from itertools import count

for el in count(int(input("введите число: "))):
    if el > 10:
        break
    else:
        print(el)
