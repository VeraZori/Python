def summa():
    sum_res = 0
    ex = False
    while ex == False:
        a = input("Введите числа или q для выхода: ").split()
        summa = 0
        for el in range(len(a)):
            if a[el] == 'q' or a[el] == 'Q':
                ex = True
                break
            else:
                try:
                    summa = summa + int(a[el])
                except:
                    print("В строке есть не число!")

        sum_res = sum_res + summa
        print(f"Промежуточная сумма {sum_res}")
    print(f"Итоговая сумма {sum_res}")


summa()
