class Stationery:
    def __init__(self, t):
        self.title = t

    def draw(self):
        print(f"Запуск отрисовки.")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск Pen.")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск Pencil.")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск Handle.")


ObjStationery = Stationery("Stationery")
ObjStationery.draw()

ObjPen = Pen("Pen")
ObjPen.draw()

ObjPencil = Pencil("Pencil")
ObjPencil.draw()

ObjHandle = Handle("Handle")
ObjHandle.draw()
