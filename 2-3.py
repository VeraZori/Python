# dict
seasons = {'зима': (1, 2, 12),
           'весна': (3, 4, 5),
           'лето': (6, 7, 8),
           'осень': (9, 10, 11)}

month = int(input('Введите номер месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

# list
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print("зима")
elif month in spring:
    print("весна")
elif month in summer:
    print("лето")
elif month in autumn:
    print("осень")
else:
    print("Нет месяца с таким порядковым номером")