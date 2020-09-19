my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for num, el in enumerate(my_list) if num !=0 if my_list[num] > my_list[num-1]]
print(f'Исходный список: {my_list}')
print(f'Ответ:значения исходника, которые больше предыдущего элемента: {new_list}')

