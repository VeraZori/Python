class ComplNumb:
    def __init__(self, d, m):
        self.d = d
        self.m = m

    def __add__(self, other):
        return f"{self.d + other.d} + {self.m + other.m}i"

    def __mul__(self, other):
        return f"{self.d * other.d - self.m * other.m} + {self.d * other.m + self.m * other.d}i"

    def __str__(self):
        return f"{self.d}+{self.m}i"


a = ComplNumb(1, 2)
b = ComplNumb(3, 4)
print(a + b)
print(a * b)
