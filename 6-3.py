class Worker:
    def __init__(self, n, sn, pos, inc):
        self.name = n
        self.surname = sn
        self.position = pos
        self._income = inc


class Position(Worker):
    def __init__(self, n, sn, pos, inc):
        super().__init__(n, sn, pos, inc)

    def get_full_name(self):
        print(f"Полное имя сотрудника {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии {sum(self._income.values())}")


n = input("Name: ")
sn = input("Surname: ")
pos = input("Position: ")
inc_wage = int(input("Wage: "))
inc_bonus = int(input("Bonus: "))
inc = {"Wage": inc_wage, "Bonus": inc_bonus}

w1 = Position(n, sn, pos, inc)
w1.get_full_name()
w1.get_total_income()
