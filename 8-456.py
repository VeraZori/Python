class Store:

    def __init__(self):
        self.dict = {}

    def get_eq(self, equipment):
        self.dict.setdefault(equipment.eq_name(), []).append(equipment)

    # pass

    def del_eq(self, eq):
        if self.dict[eq.name]:
            self.dict.setdefault(eq.name).pop()


class OfEq:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
        self.equipment = self.__class__.__name__

    def eq_name(self):
        return f"{self.equipment}"

    def __repr__(self):
        return f"{self.name} {self.price} {self.count}"


class Printer(OfEq):
    def __init__(self, name, price, count, type):
        super().__init__(name, price, count)
        self.type = type

    def __repr__(self):
        return f"{self.name} {self.price} {self.count} {self.type}"


class Scanner(OfEq):
    def __init__(self, name, price, count, color):
        super().__init__(name, price, count)
        self.color = color

    def __repr__(self):
        return f"{self.name} {self.price} {self.count} {self.color}"


class Xerox(OfEq):
    def __init__(self, name, price, count, paper):
        super().__init__(name, price, count)
        self.paper = paper

    def __repr__(self):
        return f"{self.name} {self.price} {self.count} {self.paper}"


store1 = Store()
pr1 = Printer("HP", 200, 5, "laser")
store1.get_eq(pr1)
sc1 = Scanner("Scan", 250, 2, "black")
store1.get_eq(sc1)
x1 = Xerox("Xerox", 150, 6, "A4")
store1.get_eq(x1)
x2 = Xerox("Xerox2", 150, 6, "A3")
store1.get_eq(x2)

while True:
    menu = input("1-РІС‹С…РѕРґ,2-РґРѕР±Р°РІРёС‚СЊ С‚РµС…РЅРёРєСѓ,3-СѓРґР°Р»РёС‚СЊ С‚РµС…РЅРёРєСѓ")
    if int(menu) == 1:
        break
    elif int(menu) == 2:
        menu1 = input("1-РїСЂРёРЅС‚РµСЂ, 2- СЃРєР°РЅРµСЂ, 3-РєСЃРµСЂРѕРєСЃ")
        if int(menu1) == 1:
            name = input("РЅР°Р·РІР°РЅРёРµ ")
            price = input("С†РµРЅР° ")
            count = input("РєРѕР»РёС‡РµСЃС‚РІРѕ")
            type = input("С‚РёРї СЃС‚СЂСѓР№РЅС‹Р№/Р»Р°Р·РµСЂРЅС‹Р№")
            pr = Printer(name, price, count, type)
            store1.get_eq(pr)
        elif int(menu1) == 2:
            name = input("РЅР°Р·РІР°РЅРёРµ ")
            price = input("С†РµРЅР° ")
            count = input("РєРѕР»РёС‡РµСЃС‚РІРѕ")
            type = input("С‚РёРї С†РІРµС‚РЅРѕР№/С‡РµСЂРЅРѕ-Р±РµР»С‹Р№")
            sc = Scanner(name, price, count, color)
            store1.get_eq(sc)
        elif int(menu1) == 3:
            name = input("РЅР°Р·РІР°РЅРёРµ ")
            price = input("С†РµРЅР° ")
            count = input("РєРѕР»РёС‡РµСЃС‚РІРѕ")
            type = input("С„РѕСЂРјР°С‚")
            x = Xerox(name, price, count, paper)
            store1.get_eq(x)
        else:
            break
    elif int(menu) == 3:
        print(store1.dict)
        del_equipment = input("Р’РІРµРґРёС‚Рµ РЅР°Р·РІР°РЅРёРµ РґР»СЏ СѓРґР°Р»РµРЅРёСЏ ")

print(store1.dict)