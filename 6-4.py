import random


class Car:
    def __init__(self, v, c, n, pol, dir):
        self.speed = v
        self.color = c
        self.name = n
        self.is_police = pol
        self.direction = dir

    def go(self):
        print(f"Машина {self.name} {self.color} цвет начала движение")

    def stop(self):
        print(f"Машина {self.name} {self.color} цвет остановилась")

    def turn(self):
        print(f"Машина {self.name} {self.color} цвет повернула {self.direction}")

    def show_speed(self):
        print(f"Машина {self.name} {self.color} цвет движется со скоростью {self.speed}")


class TownCar(Car):
    def __init__(self, v, c, n, pol, dir):
        super().__init__(v, c, n, pol, dir)

    def show_speed(self):
        if self.speed > 60:
            print(f"Машина {self.name} {self.color} превысила скорость!")
        else:
            print(f"Машина {self.name} {self.color} цвет движется со скоростью {self.speed}")


class SportCar(Car):
    def __init__(self, v, c, n, pol, dir):
        super().__init__(v, c, n, pol, dir)


class WorkCar(Car):
    def __init__(self, v, c, n, pol, dir):
        super().__init__(v, c, n, pol, dir)

    def show_speed(self):
        if self.speed > 40:
            print(f"Машина {self.name} {self.color} превысила скорость!")
        else:
            print(f"Машина {self.name} {self.color} цвет движется со скоростью {self.speed}")


class PoliceCar(Car):
    def __init__(self, v, c, n, pol, dir):
        super().__init__(v, c, n, pol, dir)


wc1 = WorkCar(55, "красная", "Рабочая машина1", False, random.choice(["направо", "налево"]))
wc1.go()
wc1.turn()
wc1.turn()
wc1.show_speed()
wc1.stop()

wc2 = WorkCar(35, "зеленая", "Рабочая машина2", False, random.choice(["направо", "налево"]))
wc2.go()
wc2.turn()
wc2.turn()
wc2.show_speed()
wc2.stop()

wc3 = TownCar(55, "синяя", "Городская машина3", False, random.choice(["направо", "налево"]))
wc3.go()
wc3.turn()
wc3.turn()
wc3.show_speed()
wc3.stop()

wc4 = TownCar(70, "красная", "Городская машина4", False, random.choice(["направо", "налево"]))
wc4.go()
wc4.turn()
wc4.turn()
wc4.show_speed()
wc4.stop()

wc5 = SportCar(110, "белая", "Спортивная машина5", False, random.choice(["направо", "налево"]))
wc5.go()
wc5.turn()
wc5.turn()
wc5.show_speed()
wc5.stop()

wc6 = PoliceCar(80, "серая", "Полицейская машина6", True, random.choice(["направо", "налево"]))
wc6.go()
wc6.turn()
wc6.turn()
wc6.show_speed()
wc6.stop()
