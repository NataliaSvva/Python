my_list = [7, 5, 3, 3, 2]
s = int(input("Введите число от 1 до 9:"))
my_list.append(s)
a = sorted(my_list, reverse = True)
print(f'{"Пользователь ввел число:"} {s} {".Результат:"} {str(a)[1:-1]}')