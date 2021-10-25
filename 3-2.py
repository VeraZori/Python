def info(name='', surname='', year_birth='', city='', email='', phone=''):
    print(f"{surname} {name} {year_birth} рождения, проживает в городе {city},электронная почта {email},"
          f" номер телефона {phone}")


name = input("Введите Ваше имя ")
surname = input("Введите Вашу фамилию ")
year_birth = input("Введите Ваш год рождения ")
city = input("Введите город, в котором живете ")
email = input("Введите Вашу электронную почту ")
phone = input("Введите Ваш номер телефона ")
info(name=name, surname=surname, year_birth=year_birth, city=city, email=email, phone=phone)
