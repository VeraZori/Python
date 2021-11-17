class MyExc(Exception):
    def __init__(self, text):
        self.text = text


my_list = []
while True:
    a = input("Введите число: ")
    try:
        if a == "q" or a == "Q":
            break
        elif a.isdigit() == False:
            raise MyExc("Введите число!")
        else:
            my_list.append(a)
    except MyExc as err:
        print(err)

print(my_list)
