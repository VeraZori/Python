class MyDate:
    def __init__(self):
        self.mydate = mydate

    @classmethod
    def dateToNum(cls, mydate):
        day, month, year = mydate.split("-")
        return (day, month, year)

    @staticmethod
    def validDate(mydate):
        day, month, year = MyDate.dateToNum(mydate)
        if 1 <= int(day) <= 31 and 1 <= int(month) <= 12 and 2000 <= int(year) <= 2020:
            return ("Все верно")
        else:
            return ("Дата введена неверно")


date1 = MyDate
date2 = MyDate
print(date1.dateToNum("32-09-2020"))
print(date1.validDate("32-09-2020"))
print(date2.dateToNum("20-09-2020"))
print(date2.validDate("20-09-2020"))
