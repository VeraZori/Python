goods=[]
a=int(input("Введите количество товаров "))
i=0
while a:
    i+=1
    name=input("Название товара ")
    price = input("Цена товара ")
    count = input("Количество товара ")
    unit = input("Единицы измерения ")
    a=a-1
    #el=(i,{"name":name,"price":price,"count":count,"unit":unit})
    goods.append(el)
    print(el)
listnew = []
for i in range(0,len(goods)):
    for j in range(1,len(goods[i])):
        listnew.append(goods[i][j])

keylist=listnew[0].keys()
mydata = dict((k,list(set(map(lambda d: d[k], listnew)))) for k in keylist)
print(mydata)

