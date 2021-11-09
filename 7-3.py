class Cell:
    def __init__(self, cell_count):
        self.cell_count = cell_count

    def __add__(self, other):
        return (f"Объединение 2х клеток: {int(self.cell_count) + int(other.cell_count)}")

    def __sub__(self, other):
        if (int(self.cell_count) - int(other.cell_count)) > 0:
            return (f"Вычитание 2х клеток: {int(self.cell_count) - int(other.cell_count)}")
        else:
            return ("Разность количества ячеек 2х клеток меньше 0!")

    def __mul__(self, other):
        return (f"Произведение 2х клеток: {int(self.cell_count) * int(other.cell_count)}")

    def __truediv__(self, other):
        return (f"Деление 2х клеток: {int(self.cell_count) // int(other.cell_count)}")

    def make_order(self, cell_count, cell_row):
        self.cell_row = cell_row
        cell_row_count = int(cell_count) // int(cell_row)
        for i in range(0, cell_row_count):
            print("*" * int(cell_row))
        if (int(cell_count) % int(cell_row)) != 0:
            print("*" * (int(cell_count) % int(cell_row)))


cell1 = Cell(input("Количество ячеек клетки 1: "))
cell2 = Cell(input("Количество ячеек клетки 2: "))
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
cell1.make_order(input("Количество ячеек "), input("Количество рядов "))
