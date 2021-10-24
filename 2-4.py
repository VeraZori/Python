my_list=list(input("Введите строку").split(" "))
for id, el in enumerate(my_list,1):
    print(id, el) if len(el)<=10 else print(id,el[:10])
