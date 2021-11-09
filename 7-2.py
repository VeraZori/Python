from abc import ABC, abstractmethod


class Clothes:
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def expense(self):
        pass

    def __str__(self):
        return str(self.size)


class Coat(Clothes):
    @property
    def expense(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def expense(self):
        return 2 * self.size + 0.3


coat1 = Coat(46)
suit1 = Suit(1.65)
print(f"Для пальто размера {coat1} необходимо {coat1.expense:.2f} м ткани")
print(f"Для костюма размера {suit1} необходимо {suit1.expense:.2f} м ткани")
