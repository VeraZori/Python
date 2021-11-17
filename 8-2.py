class MyExc(Exception):
    def __init__(self, text):
        self.text = text


while True:
    try:
        a = int(input("Введите делимое:"))
    except ValueError:
        print("Введите число!")
    else:
        break

while True:
    try:
        b = int(input("Введите делитель:"))
        if b == 0:
            raise MyExc("Делитель не может быть 0")
    except ValueError:
        print("Введите число!")
    except MyExc as err:
        print(err)
    else:
        break

print(a / b)
