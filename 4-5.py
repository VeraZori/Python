from functools import reduce


def func(el, el_next):
    return el * el_next


m = [n for n in range(100, 1001) if n % 2 == 0]
res = reduce(func, m)
print(res)
