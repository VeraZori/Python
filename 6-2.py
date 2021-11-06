class Road():
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def res(self):
        result = (self._length * self._width * 25 * 5) / 1000
        print(f"{result} тонн")


r = Road(int(input("Введите длину покрытия, м: ")), int(input("Введите ширину покрытия, м: ")))
r.res()
