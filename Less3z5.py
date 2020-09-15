def sum_func():
    my_sum = 0
    lst = input("Введите числа через пробел: ").split()
    for el in range(len(lst)):
        if lst[el] != "q":
            my_sum = my_sum + int(lst[el])
        else:
            break
    print(my_sum)
    if "q" in lst:
        exit("Выход из программы")
    else:
        sum_func()
sum_func()