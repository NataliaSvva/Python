my_list = [11, 12, 33, 51, 87, 25, 4, 10, 44, 55, 66, 22]
new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список: {my_list}')
print(f'Ответ:значения исходника, которые больше предыдущего элемента: {new_list}')