user_time = int(input("Введите время в секундах: "))
h = user_time // 3600
m = user_time % 3600 // 60
s = user_time % 3600 % 60
print('{:02d}:{:02d}:{:02d}'.format(h, m, s))
