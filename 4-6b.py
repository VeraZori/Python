from itertools import cycle

c = 0
for el in cycle(["a", "b", "c"]):
    if c > 10:
        break
    print(el)
    c += 1
